import streamlit as st

st.set_page_config(layout="wide", page_title="📃 Strona główna | OdrApp 💦")

st.markdown("""
<style>
.align-text {
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

# Customize page title
st.title(
    "Witaj w OdrApp! 💦"
)

st.markdown(
    """
    <p class="align-text"> <i>OdrApp</i> to aplikacja służąca do monitoringu jakości wody w rzece Odra. Przedstawia ona wieloczasową analiza jakości wody z wykorzystaniem zobrazowań satelitarnych i Google Earth Engine. Obejmuje okres od 2018 do teraz, od kwietnia do października.\n
    Eksploruj wszystkie strony do woli i dowiedz się więcej o zanieczyszczeniu wody w Odrze.</p>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("""
    #### Sugerowane działania:
    1. Przejdź do strony *Indeksy* 🌍 i dowiedz się więcej o indekach spektralnych użytych w analizie.
    2. Odwiedzaj strony indeksów:
        - 💦 - powszechnie stosowane wskaźniki,
        - 🦠 - związane stricte z zanieczyszczeniem i jakością wody.\n
        Przeglądaj mapy z wizualizacją indeksów w zakładce 🗺️ Mapa i wykres liniowy przedstawiający średnią wartość indeksów na przestrzeni analizowanego okresu w zakładce 📈 Wykres.
    3. Wejdź na stronę *Wykresy* 📈 gdzie poznasz wizualizację wyników na wykresach, tj.
        - "roczne",
        - "miesięczne",
        - okresowe,
        - z katastrofy ekologicznej Odry 2022.
    4. Na stronie *Katastrofa ekologiczna - Odra 2022* znajdziesz rozszerzoną analizę jakości wody w 4 nadrzecznych miastach: Ostravie (CZ), Wrocławiu, Frankfurcie (DE) oraz Szczecinie.

    **Kolejność dowolna! Na start, pamiętaj o przeczytaniu o indeksach spektralnych na stronie *Indeksy* 🌍.**

    ##### Miłego korzystania! 💦
    """
)
