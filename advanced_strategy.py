#!/usr/bin/env python3
"""
Stratégie Avancée Multi-Paires pour LBank Trading Bot
Analyse TOUTES les paires disponibles et choisit automatiquement la plus favorable
"""

import requests
import time
from datetime import datetime

class AdvancedMultiPairStrategy:
    """Analyse toutes les paires LBank et sélectionne la meilleure opportunité"""
    
    def __init__(self, api):
        self.api = api
        self.base_url = "https://api.lbkex.com"
        self.all_pairs = []
        self.best_pair = None
        self.analysis_results = []
    
    def log(self, message):
        """Log avec timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def get_all_trading_pairs(self):
        """
        Récupère TOUTES les paires de trading disponibles sur LBank
        """
        try:
            self.log("⌛ Chargement de toutes les paires disponibles...")
            url = f"{self.base_url}/v2/accuracy.do"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('result') == 'true':
                    # Extraire toutes les paires
                    pairs_data = data.get('data', [])
                    self.all_pairs = [pair.get('symbol') for pair in pairs_data]
                    self.log(f"✅ {len(self.all_pairs)} paires trouvées sur LBank")
                    return self.all_pairs
            
            self.log("⚠️ Impossible de charger les paires, utilisation des paires par défaut")
            # Paires populaires par défaut si l'API ne répond pas
            self.all_pairs = [
                'btc_usdt', 'eth_usdt', 'bnb_usdt', 'xrp_usdt', 'ada_usdt',
                'doge_usdt', 'sol_usdt', 'dot_usdt', 'matic_usdt', 'link_usdt',
                'uni_usdt', 'ltc_usdt', 'etc_usdt', 'atom_usdt', 'xlm_usdt',
                'eth_btc', 'bnb_btc', 'xrp_btc', 'ada_btc', 'doge_btc'
            ]
            return self.all_pairs
            
        except Exception as e:
            self.log(f"❌ Erreur lors du chargement des paires: {e}")
            return []
    
    def analyze_pair(self, pair):
        """
        Analyse une paire spécifique et calcule son score d'opportunité
        Retourne: dict avec score, volume, volatility, trend
        """
        try:
            # Récupérer les données de la paire
            url = f"{self.base_url}/v2/ticker/24hr.do"
            params = {"symbol": pair}
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code != 200:
                return None
            
            data = response.json()
            if data.get('result') != 'true':
                return None
            
            ticker_data = data.get('data', [{}])[0]
            
            # Extraire les métriques
            last_price = float(ticker_data.get('last', 0))
            high_24h = float(ticker_data.get('high', 0))
            low_24h = float(ticker_data.get('low', 0))
            volume_24h = float(ticker_data.get('vol', 0))
            change_percent = float(ticker_data.get('change', 0))
            
            if high_24h == 0 or low_24h == 0 or last_price == 0:
                return None
            
            # Calculs d'analyse
            # 1. Volatilité (plus élevée = plus d'opportunités)
            volatility = ((high_24h - low_24h) / low_24h) * 100
            
            # 2. Position dans la fourchette (0 = bas, 1 = haut)
            price_position = (last_price - low_24h) / (high_24h - low_24h)
            
            # 3. Score d'opportunité d'achat (plus élevé = meilleure opportunité d'achat)
            # On préfère: prix bas (< 0.3), haute volatilité, volume élevé, tendance positive
            buy_score = 0
            
            # Prix proche du bas = bon pour acheter (max 40 points)
            if price_position < 0.2:
                buy_score += 40
            elif price_position < 0.3:
                buy_score += 30
            elif price_position < 0.4:
                buy_score += 20
            
            # Volatilité (max 30 points)
            if volatility > 10:
                buy_score += 30
            elif volatility > 5:
                buy_score += 20
            elif volatility > 2:
                buy_score += 10
            
            # Tendance positive (max 20 points)
            if change_percent > 5:
                buy_score += 20
            elif change_percent > 2:
                buy_score += 15
            elif change_percent > 0:
                buy_score += 10
            
            # Volume (max 10 points)
            if volume_24h > 10000:
                buy_score += 10
            elif volume_24h > 1000:
                buy_score += 5
            
            return {
                'pair': pair,
                'score': buy_score,
                'last_price': last_price,
                'high_24h': high_24h,
                'low_24h': low_24h,
                'volume_24h': volume_24h,
                'volatility': volatility,
                'price_position': price_position,
                'change_percent': change_percent,
                'buy_opportunity': buy_score > 60  # Score > 60 = bonne opportunité
            }
            
        except Exception as e:
            return None
    
    def scan_all_pairs(self):
        """
        Analyse TOUTES les paires et classe par opportunité
        """
        self.log("🔍 Démarrage du scan de toutes les paires...")
        self.analysis_results = []
        
        for i, pair in enumerate(self.all_pairs):
            # Afficher la progression tous les 10 paires
            if (i + 1) % 10 == 0:
                self.log(f"Analyse en cours... {i + 1}/{len(self.all_pairs)} paires")
            
            result = self.analyze_pair(pair)
            if result:
                self.analysis_results.append(result)
            
            # Petit délai pour ne pas surcharger l'API
            time.sleep(0.1)
        
        # Trier par score (du plus élevé au plus bas)
        self.analysis_results.sort(key=lambda x: x['score'], reverse=True)
        
        self.log(f"✅ Analyse terminée: {len(self.analysis_results)} paires analysées")
        return self.analysis_results
    
    def get_best_opportunity(self):
        """
        Retourne la meilleure opportunité de trading
        """
        if not self.analysis_results:
            self.scan_all_pairs()
        
        if len(self.analysis_results) == 0:
            self.log("⚠️ Aucune opportunité trouvée")
            return None
        
        # Prendre le top 1
        best = self.analysis_results[0]
        
        self.log("\n" + "="*70)
        self.log("🏆 MEILLEURE OPPORTUNITÉ DÉTECTÉE")
        self.log("="*70)
        self.log(f"Paire: {best['pair'].upper()}")
        self.log(f"Score d'opportunité: {best['score']}/100")
        self.log(f"Prix actuel: {best['last_price']}")
        self.log(f"Volatilité: {best['volatility']:.2f}%")
        self.log(f"Variation 24h: {best['change_percent']:.2f}%")
        self.log(f"Volume 24h: {best['volume_24h']}")
        self.log(f"Position prix: {best['price_position']*100:.1f}% de la fourchette 24h")
        self.log("="*70 + "\n")
        
        self.best_pair = best['pair']
        return best
    
    def get_top_opportunities(self, n=5):
        """
        Retourne les N meilleures opportunités
        """
        if not self.analysis_results:
            self.scan_all_pairs()
        
        top_n = self.analysis_results[:n]
        
        self.log("\n" + "="*70)
        self.log(f"🏆 TOP {n} DES MEILLEURES OPPORTUNITÉS")
        self.log("="*70)
        
        for i, opp in enumerate(top_n, 1):
            self.log(f"\n{i}. {opp['pair'].upper()} - Score: {opp['score']}/100")
            self.log(f"   Prix: {opp['last_price']} | Volatilité: {opp['volatility']:.2f}% | Change: {opp['change_percent']:.2f}%")
        
        self.log("\n" + "="*70 + "\n")
        
        return top_n
    
    def should_trade(self, pair=None):
        """
        Détermine s'il faut trader (et sur quelle paire)
        Retourne: (should_trade, pair, action, price)
        """
        if pair is None:
            # Chercher la meilleure opportunité
            best = self.get_best_opportunity()
            if not best:
                return (False, None, None, None)
            
            if best['buy_opportunity']:
                return (True, best['pair'], 'buy', best['last_price'])
        else:
            # Analyser la paire spécifiée
            result = self.analyze_pair(pair)
            if result and result['buy_opportunity']:
                return (True, pair, 'buy', result['last_price'])
        
        return (False, None, None, None)


# Exemple d'utilisation
if __name__ == "__main__":
    print("🤖 Test de la Stratégie Avancée Multi-Paires\n")
    
    # Simuler une API simple pour le test
    class MockAPI:
        pass
    
    strategy = AdvancedMultiPairStrategy(MockAPI())
    
    # Charger toutes les paires
    pairs = strategy.get_all_trading_pairs()
    print(f"\n📊 {len(pairs)} paires disponibles\n")
    
    # Scanner et trouver la meilleure opportunité
    best = strategy.get_best_opportunity()
    
    # Afficher le top 5
    strategy.get_top_opportunities(5)
    
    print("✅ Test terminé!")
