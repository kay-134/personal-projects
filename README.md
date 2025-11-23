# PCOS Buddy 💜

A friendly AI chatbot that helps people recently diagnosed with PCOS understand their condition in simple, approachable terms.

## Features

- **Friendly Conversations**: Explains PCOS concepts like talking to a friend, using 7th-grade level language
- **Comprehensive Knowledge Base**: Information sourced from medical research, clinical guidelines, and community experiences
- **Topics Covered**:
  - What is PCOS and how it's diagnosed
  - Common symptoms
  - Medications (Metformin, Birth Control, Spironolactone)
  - Natural treatments and supplements (Inositol, Vitamin D, NAC, etc.)
  - Diet and exercise recommendations
  - Mental health support
  - Fertility information
  - Community tips from r/PCOS

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the web app:
   ```bash
   python app.py
   ```

3. Open your browser to `http://localhost:5000`

## CLI Mode

You can also chat in the terminal:

```bash
python chatbot.py
```

## Project Structure

```
├── app.py                  # Flask web application
├── chatbot.py              # Chatbot logic and conversation handling
├── pcos_knowledge_base.py  # PCOS information database
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Web chat interface
└── README.md
```

## Information Sources

This chatbot's knowledge base is built from:

- [2023 International PCOS Guidelines](https://academic.oup.com/jcem/article/108/10/2447/7242360)
- [Mayo Clinic - PCOS](https://www.mayoclinic.org/diseases-conditions/pcos/)
- [NHS - PCOS](https://www.nhs.uk/conditions/polycystic-ovary-syndrome-pcos/)
- [WHO - PCOS Fact Sheet](https://www.who.int/news-room/fact-sheets/detail/polycystic-ovary-syndrome)
- [PMC Research Studies](https://pmc.ncbi.nlm.nih.gov/)
- Community experiences from r/PCOS

## Disclaimer

This chatbot provides general information about PCOS for educational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider about your specific situation.

## License

MIT License
