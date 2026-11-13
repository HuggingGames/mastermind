---
title: Mastermind
emoji: 🎮
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: mit
---

# 🎮 Mastermind

**Hugging Games** · Yapımcı / Creator: **CAN YILDIRIM**

Dört haneli gizli kodu bul.

## 🌐 Live web demo (Hugging Face Spaces)

1. Hugging Face üzerinde **New Space** oluşturun ve **Gradio** SDK seçin.
2. Bu deponun tüm dosyalarını Space'e yükleyin.
3. Space otomatik olarak `app.py` dosyasını çalıştırır.

> Hugging Face Space bağlantısı yayınlandıktan sonra buraya eklenebilir.

## 💻 Terminalde çalıştırma

Python 3.10+ kurulu olmalı. Harici paket gerekmez:

```bash
python main.py
```

Komutları ekranda gösterildiği gibi girin. `reset` yeni oyun başlatır; `quit` çıkış yapar.

## 🌍 Web arayüzünde çalıştırma

```bash
pip install -r requirements.txt
python app.py
```

Gradio arayüzü tarayıcınızda açılır.

## 📁 Dosyalar

- `game.py`: Oyun kuralları ve durum makinesi
- `main.py`: Terminalden oynama
- `app.py`: Gradio web arayüzü / Hugging Face Spaces
- `tests/test_smoke.py`: Basit başlangıç testi
- `.github/FUNDING.yml`: Buy Me a Coffee bağışı

## ☕ Support

[Buy Me a Coffee — Hugging Games](https://buymeacoffee.com/hugginggames)

## 📝 License

MIT — © 2026 CAN YILDIRIM / Hugging Games.
