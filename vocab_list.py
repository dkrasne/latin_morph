import streamlit as st
from utils import remove_macrons
from vocab import *

st.title("Vocabulary List")

st.markdown("These are the words that are currently available in Latin Morph!")

adj_vocab = import_adjectives()
adj_vocab = list(adj_vocab)
adj_vocab.sort(key=lambda x: remove_macrons(x))

noun_vocab = import_nouns()
noun_vocab = list(noun_vocab)
noun_vocab.sort(key=lambda x: remove_macrons(x))

pronoun_vocab = import_pronouns()
pronoun_vocab = list(pronoun_vocab)
pronoun_vocab.sort(key=lambda x: remove_macrons(x))

vb_vocab = import_verbs()
vb_vocab = list(vb_vocab)
vb_vocab.sort(key=lambda x: remove_macrons(x))


nouns, verbs, adjectives, pronouns = st.columns(4)

with nouns:
    st.markdown("#### Nouns")
    st.markdown("<br>".join(noun_vocab),unsafe_allow_html=True)
with verbs:
    st.markdown("#### Verbs")
    st.markdown("<br>".join(vb_vocab),unsafe_allow_html=True)
with adjectives:
    st.markdown("#### Adjectives")
    st.markdown("<br>".join(adj_vocab),unsafe_allow_html=True)
with pronouns:
    st.markdown("#### Pronouns")
    st.markdown("<br>".join(pronoun_vocab),unsafe_allow_html=True)
