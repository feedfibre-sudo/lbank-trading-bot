# 🚀 Guide de Déploiement - LBank Trading Bot

## ✅ Bot 100% Prêt et Testé

Votre bot de trading automatique est **complètement fonctionnel** et hébergé sur ce repository GitHub.

### 📦 Fichiers du projet:
- `advanced_strategy.py` - Bot intelligent avec analyse multi-marchés
- `bot.py` - Bot de base simple
- `requirements.txt` - Dépendances Python
- `Dockerfile` - Configuration pour déploiement cloud
- `.env.example` - Template pour clés API

---

## 🎯 HÉBERGEMENT GRATUIT - HidenCloud (Recommandé)

### Pourquoi HidenCloud?
✅ **100% GRATUIT** (€0.00/semaine)
✅ Support Python complet
✅ 3GB RAM, 2 CPU cores, 15GB storage
✅ Uptime 99.9%
✅ Support 24/7
✅ Renouvellement hebdomadaire GRATUIT

### 📝 Étapes de déploiement:

#### 1. Inscription HidenCloud
1. Allez sur: https://dash.hidencloud.com/auth/register
2. Créez votre compte
3. Validez votre email
4. **Connectez votre compte Discord** (requis pour anti-abus)

#### 2. Commander le serveur gratuit
1. Dashboard → Services → Order new service
2. Sélectionnez "Free Hosting" → "Free Server"
3. Confirmez (€0.00)
4. Attendez la création du serveur (~5 minutes)

#### 3. Déployer le bot
```bash
# SSH vers votre serveur HidenCloud
ssh root@votre-serveur.hidencloud.com

# Cloner le repository
git clone https://github.com/feedfibre-sudo/lbank-trading-bot.git
cd lbank-trading-bot

# Installer Python et pip
apt update
apt install python3 python3-pip -y

# Installer les dépendances
pip3 install -r requirements.txt

# Configurer les clés API
cp .env.example .env
nano .env
# Ajoutez vos clés API LBank:
# API_KEY=votre_cle_api
# API_SECRET=votre_secret_api

# Lancer le bot
python3 advanced_strategy.py
```

#### 4. Exécution en arrière-plan (24/7)
```bash
# Installer screen pour garder le bot actif
apt install screen -y

# Créer une session screen
screen -S lbank-bot

# Lancer le bot
python3 advanced_strategy.py

# Détacher la session: Ctrl+A puis D
# Réattacher plus tard: screen -r lbank-bot
```

---

## 🔑 Configuration des clés API LBank

### Créer des clés API:
1. Connectez-vous sur https://www.lbank.com
2. Compte → API Management
3. Créez une nouvelle clé API
4. **Activez uniquement le trading** (pas de retrait)
5. Notez votre API Key et Secret

### Sécurité:
- ✅ N'activez QUE le trading
- ✅ Désactivez les retraits
- ✅ Utilisez une whitelist IP si possible
- ✅ Ne partagez JAMAIS vos clés

---

## 🎮 Utilisation du Bot

### Mode automatique (Recommandé)
Le bot `advanced_strategy.py` analyse automatiquement TOUS les marchés LBank et trade sur la paire la plus rentable.

```bash
python3 advanced_strategy.py
```

**Le bot va:**
1. Scanner tous les marchés LBank
2. Calculer un score pour chaque paire (volume + volatilité + spread)
3. Sélectionner automatiquement la meilleure
4. Exécuter des trades optimisés
5. Répéter toutes les 5 minutes

### Mode manuel
```bash
python3 bot.py
```

---

## 📊 Monitoring

### Vérifier que le bot tourne:
```bash
screen -ls  # Liste les sessions
screen -r lbank-bot  # Se reconnecter
```

### Logs en temps réel:
Le bot affiche:
- Marchés analysés
- Scores calculés
- Paire sélectionnée
- Trades exécutés
- Profits/pertes

---

## 🔄 Renouvellement Hebdomadaire

⚠️ **Important**: HidenCloud nécessite un renouvellement GRATUIT chaque semaine.

1. Connectez-vous à https://dash.hidencloud.com
2. Services → Votre serveur
3. Cliquez sur "Renew" (gratuit)
4. Le bot continue de fonctionner

---

## 🆘 Dépannage

### Le bot ne démarre pas
```bash
# Vérifier Python
python3 --version

# Réinstaller les dépendances
pip3 install -r requirements.txt --force-reinstall
```

### Erreur de connexion API
- Vérifiez vos clés dans `.env`
- Assurez-vous que les clés sont actives sur LBank
- Vérifiez votre connexion internet

### Le bot s'arrête
```bash
# Relancer dans screen
screen -S lbank-bot
python3 advanced_strategy.py
# Ctrl+A puis D pour détacher
```

---

## 📈 Optimisation

### Ajuster la stratégie:
Éditez `advanced_strategy.py`:
```python
# Ligne ~50: Ajuster les poids du score
score = (volume * 0.4) + (volatility * 0.3) + (1/spread * 0.3)
```

### Changer l'intervalle:
```python
# Ligne ~100: Modifier le délai entre les analyses
time.sleep(300)  # 300 secondes = 5 minutes
```

---

## ⚠️ Avertissement

Ce bot est fourni à des fins éducatives. Le trading comporte des risques. L'auteur n'est pas responsable des pertes financières. Tradez à vos propres risques.

---

## 🎉 Vous êtes prêt!

Votre bot de trading LBank est maintenant déployé et fonctionne 24/7 gratuitement sur HidenCloud!

**Bon trading! 🚀💰**
