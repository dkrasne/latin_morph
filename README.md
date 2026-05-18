[Latin Morph!](https://latin-morph.streamlit.app/) is a [Streamlit](https://streamlit.io/) app that allows Latin students of all levels to practice their morphology by creating correct word forms for different parts of speech (nouns, verbs, pronouns, and adjectives). Settings can be adjusted for a given part of speech in order to only practice a small set of forms (e.g., just first declension nouns, or just future active verbs), or to allow practice across a larger set of forms. For logged-in users, their settings and answers are stored in a [Supabase](https://supabase.com/) database.

Forms and questions are generated on the fly, rather than drawing on a preset list, so it is not possible to run out of questions. There is a rudimentary adaptive learning algorithm so that students are tested more frequently on things that they tend to get wrong. The [available vocabulary](./vocab.py) is limited but can easily be extended upon request.

&copy; 2026 Darcy Krasne ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/))

![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white) [![Made with Supabase](https://supabase.com/badge-made-with-supabase-dark.svg)](https://supabase.com)

