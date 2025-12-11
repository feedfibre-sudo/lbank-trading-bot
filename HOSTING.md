# 🌐 Options d'Hébergement Gratuit pour le Bot de Trading LBank

Ce document liste toutes les options d'hébergement gratuit disponibles pour déployer votre bot de trading automatique LBank.

---

## ✅ Options Recommandées (100% Gratuites)

### 1. **Koyeb** ⭐ MEILLEUR CHOIX

**Avantages:**
- ✅ Vraiment gratuit (pas de carte bancaire requise)
- ✅ 1 service web gratuit
- ✅ 512 MB RAM + 0.1 vCPU
- ✅ Déploiement depuis GitHub automatique
- ✅ Certificat SSL automatique
- ✅ Infrastructure haute performance

**Limitations:**
- ⚠️ Scale-to-zero en cas d'inactivité (mais redémarre automatiquement)
- ⚠️ Requiert vérification email

**Comment déployer:**
```bash
1. Créer un compte sur https://www.koyeb.com (avec GitHub OAuth)
2. Vérifier votre email
3. Créer un nouveau service:
   - Source: GitHub → sélectionner feedfibre-sudo/lbank-trading-bot
   - Builder: Dockerfile
   - Instance: Free (512MB)
4. Ajouter vos variables d'environnement:
   - LBANK_API_KEY=votre_cle
   - LBANK_SECRET_KEY=votre_secret
5. Déployer!
```

**URL:** https://www.koyeb.com  
**Documentation:** https://www.koyeb.com/docs

---

### 2. **HidenCloud**

**Avantages:**
- ✅ Hébergement Python gratuit
- ✅ Scripts 24/7
- ✅ Pas de limite de temps
- ✅ Support Python complet

**Limitations:**
- ⚠️ Requiert vérification Discord
- ⚠️ Ressources limitées

**Comment déployer:**
```bash
1. Créer un compte sur https://dash.hidencloud.com
2. Vérifier votre email Discord
3. Commander un serveur Python gratuit
4. SSH vers le serveur:
   ssh user@server_ip
5. Cloner le repo:
   git clone https://github.com/feedfibre-sudo/lbank-trading-bot.git
   cd lbank-trading-bot
6. Exécuter l'installation:
   bash install.sh
7. Le bot démarre automatiquement!
```

**URL:** https://www.hidencloud.com/service/free-python-hosting  
**Statut:** Compte créé, en attente de vérification Discord

---

### 3. **GitHub Actions** (Pour scripts planifiés)

**Avantages:**
- ✅ 2000 minutes gratuites par mois
- ✅ Parfait pour les stratégies qui n'ont pas besoin de tourner en continu
- ✅ Facile avec cron jobs

**Limitations:**
- ❌ Ne convient PAS pour du trading 24/7
- ⚠️ Seulement pour des exécutions planifiées

**Comment utiliser:**
Créez `.github/workflows/trading.yml`:
```yaml
name: Trading Bot
on:
  schedule:
    - cron: '0 */4 * * *'  # Toutes les 4 heures
  workflow_dispatch:

jobs:
  trade:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run bot
        env:
          LBANK_API_KEY: ${{ secrets.LBANK_API_KEY }}
          LBANK_SECRET_KEY: ${{ secrets.LBANK_SECRET_KEY }}
        run: python bot.py
```

---

## ⚠️ Options avec Limitations

### 4. **Replit** (Nécessite keep-alive)

**Avantages:**
- ✅ Interface web intuitive
- ✅ Gratuit pour commencer

**Limitations:**
- ❌ Suspend après inactivité
- ⚠️ Nécessite UptimeRobot pour ping 24/7
- ⚠️ Ressources limitées

**Setup:**
1. Importer depuis GitHub
2. Ajouter secrets dans .env
3. Utiliser UptimeRobot (gratuit) pour ping l'URL toutes les 5 min

**URL:** https://replit.com

---

### 5. **Render** 

**Avantages:**
- ✅ Bon pour production
- ✅ Déploiement depuis GitHub

**Limitations:**
- ❌ Background Workers nécessitent plan payant ($7/mois)
- ⚠️ Web Services gratuits ont spin-down après 15min

**URL:** https://render.com

---

### 6. **Railway**

**Avantages:**
- ✅ Excellent DX (Developer Experience)

**Limitations:**
- ❌ Trial gratuit limité aux databases seulement
- ❌ Services nécessitent plan payant

**URL:** https://railway.app

---

## ❌ Options NON Recommandées

### PythonAnywhere
- ❌ Bloque les connexions API externes (WhiteList payante)
- ❌ Ne peut pas se connecter à LBank

### InfinityFree
- ❌ Pas de support Python
- ❌ PHP seulement

### Heroku
- ❌ Plus de tier gratuit depuis Nov 2022

---

## 🎯 Recommandation Finale

**Pour 24/7 gratuit:**
1. **Koyeb** (le meilleur)
2. **HidenCloud** (alternative solide)

**Pour scripts planifiés:**
- **GitHub Actions**

**Si budget disponible:**
- Render ($7/mois)
- Railway ($5/mois)

---

## 📊 Comparaison Rapide

| Plateforme | Gratuit 24/7 | RAM | CPU | Facile | Score |
|------------|--------------|-----|-----|--------|-------|
| Koyeb | ✅ | 512MB | 0.1 | ⭐⭐⭐⭐⭐ | 9/10 |
| HidenCloud | ✅ | Limited | Limited | ⭐⭐⭐⭐ | 7/10 |
| GitHub Actions | ❌ | - | - | ⭐⭐⭐⭐⭐ | 6/10 |
| Replit | ⚠️ | 512MB | 0.5 | ⭐⭐⭐ | 5/10 |
| Render | ❌ | - | - | ⭐⭐⭐⭐ | 4/10 |
| Railway | ❌ | - | - | ⭐⭐⭐⭐⭐ | 3/10 |

---

## 🚀 Démarrage Rapide

**Option 1: Koyeb (Recommandé)**
```bash
1. https://www.koyeb.com → Sign up with GitHub
2. Vérifier email
3. New Service → GitHub → feedfibre-sudo/lbank-trading-bot
4. Ajouter variables: LBANK_API_KEY, LBANK_SECRET_KEY
5. Deploy!
```

**Option 2: HidenCloud**
```bash
1. https://dash.hidencloud.com → Register
2. Vérifier Discord email
3. Order free Python server
4. SSH + git clone + bash install.sh
```

---

## 📝 Variables d'Environnement Requises

Pour tous les hébergements, vous devez configurer:

```bash
LBANK_API_KEY=votre_cle_api_lbank
LBANK_SECRET_KEY=votre_cle_secrete_lbank
```

**Comment obtenir vos clés API LBank:**
1. Connectez-vous à https://www.lbank.com
2. Account → API Management
3. Create API Key
4. Copiez API Key et Secret Key
5. **IMPORTANT:** Activez "Trade" permissions

---

## 🔒 Sécurité

⚠️ **NE JAMAIS** commiter vos clés API dans Git!

✅ Toujours utiliser:
- Variables d'environnement
- Fichier `.env` (dans .gitignore)
- Secrets du provider (GitHub Secrets, Koyeb Env Vars, etc.)

---

## 📞 Support

Problèmes d'hébergement? Créez une issue sur GitHub:
https://github.com/feedfibre-sudo/lbank-trading-bot/issues

---

**Dernière mise à jour:** Février 2025  
**Status:**
- ✅ GitHub Pages activé: https://feedfibre-sudo.github.io/lbank-trading-bot/
- ⏳ Koyeb: En attente vérification email
- ⏳ HidenCloud: En attente vérification Discord
