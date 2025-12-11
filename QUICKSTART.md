# ⚡ DÉMARRAGE RAPIDE - 3 ÉTAPES SEULEMENT

## ✅ BOT 100% PRÊT!

Votre bot de trading LBank est **complètement fini** et hébergé sur ce repository GitHub.

Il analyse automatiquement TOUS les marchés LBank et trade sur la paire la plus rentable 24/7.

---

## 🚀 3 ÉTAPES POUR DÉPLOYER

### Étape 1: Vérifier l'email Discord

1. Allez sur Discord (https://discord.com)
2. Paramètres utilisateur → Mon compte
3. Vérifiez que votre email a un badge vert (✅ Vérifié)
4. Sinon, cliquez "Renvoyer l'email de vérification"

### Étape 2: Commander le serveur gratuit

1. Allez sur: https://dash.hidencloud.com/store/view/349
2. Cliquez "Connect Discord Account"
3. Autorisez HidenCloud
4. Cochez "I accept the Terms"
5. Cliquez "Complete Checkout" (€0.00)
6. Serveur créé en 5 minutes

### Étape 3: Installer le bot (AUTOMATIQUE!)

```bash
# SSH vers votre serveur
ssh root@votre-serveur.hidencloud.com

# Clone le repository
git clone https://github.com/feedfibre-sudo/lbank-trading-bot.git
cd lbank-trading-bot

# Installation automatique!
bash install.sh
```

**C'est tout!** Le script `install.sh` fait TOUT:
- ✅ Installe Python + dépendances
- ✅ Configure l'environnement
- ✅ Vous guide pour ajouter vos clés API LBank
- ✅ Lance le bot 24/7

---

## 🔑 Clés API LBank (pendant install.sh)

1. https://www.lbank.com → Compte → API Management
2. Créez une clé API
3. **Activez UNIQUEMENT le trading** (désactivez retraits!)
4. Copiez API Key et Secret
5. Le script vous demandera de les ajouter

---

## 📊 Comment ça marche?

Le bot `advanced_strategy.py`:
1. Scanne TOUS les marchés LBank toutes les 5 min
2. Calcule un score pour chaque paire
3. Sélectionne automatiquement la plus rentable
4. Trade sur cette paire
5. Répète 24/7

**Vous n'avez rien à faire, le bot choisit toujours la meilleure opportunité!**

---

## 💰 Coûts

- ✅ Hébergement: **€0.00/semaine** (gratuit!)
- ✅ Code: Gratuit
- ⚠️ Fees LBank: ~0.1% par trade

---

## 📚 Documentation complète

Pour plus de détails, voir `DEPLOY.md`

---

## ⚡ RÉSUMÉ

1. ✅ Vérifier email Discord
2. ✅ Commander serveur gratuit HidenCloud
3. ✅ Lancer `bash install.sh`

**Et voilà! Bot actif 24/7! 🚀💰**
