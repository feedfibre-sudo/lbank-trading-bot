#!/usr/bin/env python3
"""
LBank Trading Bot - Bot de trading automatique
Créé pour automatiser le trading sur LBank Exchange
"""

import os
import sys
import time
import hmac
import hashlib
import requests
from datetime import datetime
import json

class LBankAPI:
    """Classe pour interagir avec l'API LBank"""
    
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = "https://api.lbkex.com"
    
    def _sign(self, params):
        """Génère la signature pour l'authentification"""
        sorted_params = sorted(params.items())
        query_string = '&'.join([f"{k}={v}" for k, v in sorted_params])
        query_string += f"&secret_key={self.secret_key}"
        return hashlib.md5(query_string.encode('utf-8')).hexdigest().upper()
    
    def get_ticker(self, symbol="eth_btc"):
        """Récupère les informations de prix pour une paire"""
        try:
            url = f"{self.base_url}/v2/ticker/24hr.do"
            params = {"symbol": symbol}
            response = requests.get(url, params=params, timeout=10)
            return response.json()
        except Exception as e:
            print(f"Erreur lors de la récupération du ticker: {e}")
            return None
    
    def get_account_info(self):
        """Récupère les informations du compte"""
        try:
            url = f"{self.base_url}/v2/user_info.do"
            params = {
                "api_key": self.api_key,
                "timestamp": str(int(time.time() * 1000))
            }
            params["sign"] = self._sign(params)
            response = requests.post(url, data=params, timeout=10)
            return response.json()
        except Exception as e:
            print(f"Erreur lors de la récupération du compte: {e}")
            return None
    
    def place_order(self, symbol, order_type, price, amount):
        """Place un ordre de trading"""
        try:
            url = f"{self.base_url}/v2/create_order.do"
            params = {
                "api_key": self.api_key,
                "symbol": symbol,
                "type": order_type,  # buy ou sell
                "price": str(price),
                "amount": str(amount),
                "timestamp": str(int(time.time() * 1000))
            }
            params["sign"] = self._sign(params)
            response = requests.post(url, data=params, timeout=10)
            return response.json()
        except Exception as e:
            print(f"Erreur lors du placement de l'ordre: {e}")
            return None

class TradingBot:
    """Bot de trading automatique avec stratégie simple"""
    
    def __init__(self, api_key, secret_key):
        self.api = LBankAPI(api_key, secret_key)
        self.is_running = False
        self.trading_pair = "eth_btc"
        self.check_interval = 60  # Vérifier toutes les 60 secondes
        
    def log(self, message):
        """Affiche un message avec timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def analyze_market(self):
        """Analyse simple du marché"""
        ticker = self.api.get_ticker(self.trading_pair)
        if not ticker or ticker.get('result') != 'true':
            return None
        
        data = ticker.get('data', [{}])[0]
        return {
            'last_price': float(data.get('last', 0)),
            'high': float(data.get('high', 0)),
            'low': float(data.get('low', 0)),
            'volume': float(data.get('vol', 0))
        }
    
    def trading_strategy(self, market_data):
        """Stratégie de trading simple (à personnaliser)"""
        if not market_data:
            return None
        
        last_price = market_data['last_price']
        high = market_data['high']
        low = market_data['low']
        
        # Stratégie simple: acheter si proche du bas, vendre si proche du haut
        range_size = high - low
        if range_size == 0:
            return None
        
        position = (last_price - low) / range_size
        
        if position < 0.3:  # Prix dans les 30% bas
            return {'action': 'buy', 'price': last_price}
        elif position > 0.7:  # Prix dans les 30% hauts
            return {'action': 'sell', 'price': last_price}
        
        return None
    
    def run(self):
        """Lance le bot de trading"""
        self.is_running = True
        self.log(f"Bot de trading démarré pour {self.trading_pair}")
        
        while self.is_running:
            try:
                # Analyser le marché
                market_data = self.analyze_market()
                if market_data:
                    self.log(f"Prix actuel: {market_data['last_price']} | "
                            f"H: {market_data['high']} | L: {market_data['low']}")
                    
                    # Exécuter la stratégie
                    signal = self.trading_strategy(market_data)
                    if signal:
                        self.log(f"Signal détecté: {signal['action'].upper()} à {signal['price']}")
                        # Pour la démo, on ne place pas vraiment d'ordre
                        # self.api.place_order(self.trading_pair, signal['action'], signal['price'], 0.01)
                
                # Attendre avant la prochaine vérification
                time.sleep(self.check_interval)
                
            except KeyboardInterrupt:
                self.log("Arrêt du bot demandé par l'utilisateur")
                self.stop()
            except Exception as e:
                self.log(f"Erreur: {e}")
                time.sleep(self.check_interval)
    
    def stop(self):
        """Arrête le bot"""
        self.is_running = False
        self.log("Bot arrêté")

def main():
    """Fonction principale"""
    print("="*50)
    print("LBank Trading Bot - Version 1.0")
    print("="*50)
    
    # Charger les clés API depuis les variables d'environnement
    api_key = os.getenv('LBANK_API_KEY', '')
    secret_key = os.getenv('LBANK_SECRET_KEY', '')
    
    if not api_key or not secret_key:
        print("\n⚠️  ATTENTION: Clés API manquantes!")
        print("\nPour utiliser ce bot en mode réel:")
        print("1. Créez vos clés API sur LBank")
        print("2. Définissez les variables d'environnement:")
        print("   export LBANK_API_KEY='votre_cle_api'")
        print("   export LBANK_SECRET_KEY='votre_cle_secrete'")
        print("\nMode DEMO activé (aucun ordre réel ne sera passé)\n")
        api_key = "demo_key"
        secret_key = "demo_secret"
    
    # Créer et lancer le bot
    bot = TradingBot(api_key, secret_key)
    
    try:
        bot.run()
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
