# 🤖 LBank Trading Bot

**Bot de trading automatique et intuitif pour LBank Exchange**

🌟 Analyse les marchés en temps réel et exécute des stratégies de trading automatiques pour maximiser vos profits sur LBank.

---

## ✨ Fonctionnalités

- ✅ **Trading Automatique 24/7** - Le bot surveille le marché en continu
- 📊 **Analyse de Marché** - Analyse en temps réel des prix et tendances
- 🎯 **Stratégies Personnalisables** - Adaptez la stratégie à votre profil
- 🔒 **Sécurité** - Vos clés API sont stockées localement
- 💻 **Mode Démo** - Testez sans risque avant le trading réel
- 📦 **Facile à Déployer** - Instructions complètes pour l'hébergement

---

## 🚀 Installation Rapide

### 1. Cloner le Repository

```bash
git clone https://github.com/feedfibre-sudo/lbank-trading-bot.git
cd lbank-trading-bot
```

### 2. Installer les Dépendances

```bash
pip install -r requirements.txt
```

### 3. Configuration

Copiez le fichier `.env.example` en `.env` et ajoutez vos clés API LBank :

```bash
cp .env.example .env
```

Éditez `.env` avec vos informations :

```env
LBANK_API_KEY=votre_cle_api
LBANK_SECRET_KEY=votre_cle_secrete
TRADING_PAIR=eth_btc
DEMO_MODE=true
```

### 4. Lancer le Bot

```bash
python bot.py
```

---

## 🔑 Obtenir vos Clés API LBank

1. Connectez-vous à [LBank](https://www.lbank.com/)
2. Allez dans **Paramètres** > **API Management**
3. Créez une nouvelle clé API
4. **Important** : N'activez que les permissions de trading (pas de retrait !)
5. Copiez votre `API Key` et `Secret Key`

---

## 🎯 Stratégie de Trading

Le bot utilise une stratégie simple mais efficace :

- **Achat** : Quand le prix est dans les 30% bas de la fourchette 24h
- **Vente** : Quand le prix est dans les 30% hauts de la fourchette 24h

💡 **Personnalisable** : Modifiez la fonction `trading_strategy()` dans `bot.py` pour implémenter vos propres stratégies !

---

## ☁️ Hébergement 24/7

### Option 1 : PythonAnywhere (Recommandé)

**Coût** : 5$/mois

1. Créez un compte sur [PythonAnywhere](https://www.pythonanywhere.com/)
2. Uploadez vos fichiers
3. Installez les dépendances
4. Configurez une tâche planifiée

### Option 2 : VPS (DigitalOcean, Hetzner, etc.)

**Coût** : à partir de 5$/mois

```bash
# Sur votre VPS
git clone https://github.com/feedfibre-sudo/lbank-trading-bot.git
cd lbank-trading-bot
pip install -r requirements.txt

# Lancer en arrière-plan
nohup python bot.py &
```

### Option 3 : Serveur Local

Lancez le bot sur votre ordinateur (doit rester allumé) :

```bash
python bot.py
```

---

## ⚠️ Avertissements Importants

- 🚨 **RISQUE** : Le trading de crypto-monnaies comporte des risques. N'investissez que ce que vous pouvez vous permettre de perdre.
- 🛡️ **TESTEZ EN MODE DÉMO** : Utilisez toujours `DEMO_MODE=true` pour tester avant le trading réel
- 🔒 **SÉCURITÉ** : Ne partagez JAMAIS vos clés API
- 📊 **MONITORING** : Surveillez régulièrement les performances du bot

---

## 📚 Documentation API LBank

- [Documentation Officielle LBank API](https://www.lbank.com/docs/index.html)
- Endpoints supportés : Market Data, Trading, Account Info

---

## 🐛 Dépannage

### Le bot ne se connecte pas

- Vérifiez que vos clés API sont correctes
- Assurez-vous que l'API a les permissions de trading

### Erreurs d'installation

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

---

## 📧 Support

Pour toute question ou problème, ouvrez une [Issue](https://github.com/feedfibre-sudo/lbank-trading-bot/issues).

---

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## ⭐ Disclaimer

Ce bot est fourni à des fins éducatives. L'auteur n'est pas responsable des pertes financières. Utilisez-le à vos propres risques.

---

**🚀 Bon trading avec LBank Bot !**
