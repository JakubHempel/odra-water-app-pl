import streamlit as st

st.set_page_config(page_title="Indeksy 🌍 | OdrApp 💦")

st.markdown("""
<style>
.index-font-1 {
    font-size: 17px;
    color: #20B2AA;
}
.index-font-2 {
    font-size: 17px;
    color: #B6D79A;    
}
.align-text {
    text-align: justify;
}
li {
    color: lightgray;
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("Indeksy spektralne")
st.subheader("\n")
st.markdown("""<p class="align-text"> Zobrazowania satelitarne pochodzą z satelity Sentinel-2 Level-2A. Są to multispektralne zdjęcia o wysokiej rozdzielczości przestrzennej - 10 metrów (Google Earth Engine Data Catalog 2023) pochodzące z misji przeprowadzanej przez Europejską Agencję Kosmiczną - ESA.
\n *Podane poniżej wzory indeksów oraz długości fal centralnych oparte są na kanałach satelity z [Sentinel Online User Guide](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi/resolutions/spectral).*</p>""", unsafe_allow_html=True)
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-1"> <b>NDWI</b> (<i>Normalized Difference Water Index</i>)</span> - stosowany jest do detekcji wody na obrazach satelitarnych. Wartości NDWI powyżej zera reprezentują wodę, natomiast wartości mniejsze lub równe zero wskazują na tereny bez występowania wody (McFeeters 1996). Na zdjęciu satelitarnym jest wiele pikseli, które są złożone z wody ale również z roślinności oraz rzucanej przez niej cienia, dlatego wartości indeksu mogą różnić się od idealnego stanu, wskazującego występowanie wody. Równanie opiera się na kanałach spektralnych, których środkowe długości fal wynoszą dla pasma zielonego (Green - B3) - 560 nm i dla NIR (B8) - 832 nm.</p>""", unsafe_allow_html=True)
st.latex(r'''NDWI = \frac{Green - NIR}{Green + NIR} = \frac{B3 - B8}{B3 + B8}''')
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-1"> <b>NDVI</b> (<i>Normalized Difference Vegetation Index</i>)</span> - ma szerokie zastosowanie w monitoringu wegetacji (Yang i in. 2010), ocenie upraw (El-Shikha i in. 2007), monitoringu suszy (Yamaguchi i in. 2010) oraz ocenie suszy rolniczej (Zhang i in. 2009). Kiedy ze względów środowiskowych, tj. susza, zmniejsza się zawartość wody w glebie, roślinność zielona ma tendencję do obumierania, co prowadzi do spadku wartości NDVI (Meera Gandhi i in. 2015). Jest to prosta operacja matematyczna na pasmach NIR i czerwonego (Red).</p>""", unsafe_allow_html=True)
st.latex(r'''NDVI = \frac{NIR - Red}{NIR + Red} = \frac{B8 - B4}{B8 + B4}''')
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-1"> <b>NDSI</b> (<i>Normalized Difference Salinity Index</i>)</span> - wskaźnik ten używany jest do kontroli zasolenia gleby i wody. Woda służąca do nawadniania o dużym zasoleniu ogranicza wzrost roślin uprawnych oraz sprawia, że gleba nie nadaje się do upraw różnorodnych roślin rolniczych (Mahmuduzzaman i in. 2014). Dla przykładu, w niektórych regionach przybrzeżnych, przewiduje się, że ze względu na wzrost zasolenia wody, nawadniana produkcja rolna może zmniejszyć się o od 25% do 50% (Clarke i in. 2015). Pokazuje to, jak ważne jest stałe monitorowanie zasolenia wody i gleby.</p>""", unsafe_allow_html=True)
st.latex(r'''NDSI = \frac{SWIR1 - SWIR2}{SWIR1 + SWIR2} = \frac{B11 - B12}{B11 + B12}''')
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-2"> <b>SABI</b> (<i>Surface Algal Bloom Index</i>)</span> - został opracowany przez (Alawadi 2010) w celu identyfikacji obecności biomasy w wodzie przy użyciu pasma NIR, które jest wrażliwe na rośliny zielone, pasma niebieskiego (Blue), reagującego na czystą wodę, i pasma zielonego (Green), które wykrywa zakwity glonów w wodzie. Zjawisko zakwitu glonów występuje najczęściej, gdy istnieją odpowiednie warunki nasłonecznienia, wysoka temperatura wody i wysoki poziom składników odżywczych. Co więcej, wody wysoce eutroficzne mogą pomóc w żerowaniu glonów ze względu na wysoką zawartość azotu i fosforu (Caballeto i in. 2020). Zakres wartości wskaźnika dla wody wynosi od -0.1 do 0, a dla mikroalg poniżej lub równo -0.2 (Kulawiak 2016).</p>""", unsafe_allow_html=True)
st.latex(r'''SABI = \frac{NIR - Red}{Blue + Green} = \frac{B8 - B4}{B2 + B3}''')
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-2"> <b>CGI</b> (<i>Chlorophyll Green Index</i>)</span> - wskaźnik chlorofilu stosuje się do określenia całkowitej ilości chlorofilu w roślinach. Ta odmiana wykorzystuje w obliczeniach kanały: SWIR (rozdzielczość przestrzenna - 60 metrów i długość fali centralnej - 945 nm) i pasmo zielone Green.</p>""", unsafe_allow_html=True)
st.latex(r'''CGI = \frac{SWIR}{Green}-1 = \frac{B9}{B3}-1''')
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-2"> <b>CDOM</b> (<i>Colored Dissolved Organic Matter</i>)</span> - jest wskaźnikiem jakości wody służącym do optycznej oceny aktywnych substancji organicznych w wodzie. Na ten parametr wpływają dwa główne źródła materii organicznej. Pierwszym źródłem jest materiał organiczny, który tworzy się w samym zbiorniku wodnym, np. fotoplankton. Drugim źródłem jest materia organiczna przedostająca się do wody ze źródeł zewnętrznych, np. węgiel, nawozy, które mogą zostać wypłukiwane z otaczającej gleby. Wykazano także, że istnieje korelacja pomiędzy zawartością metylortęci a CDOM w rzekach (Fichot i in. 2016).</p>""", unsafe_allow_html=True)
st.latex(r'''CDOM = 537 \cdot \exp\left(-2.93 \cdot \frac{Green}{Red}\right) = 537 \cdot \exp\left(-2.93 \cdot \frac{B3}{B4}\right)''')
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-2"> <b>DOC</b> (<i>Dissolved Organic Carbon</i>)</span> - odnosi się do obecności organicznych związków węgla rozpuszczonych w wodzie. Służy jako kluczowy wskaźnik jakości wody, gdzie wyższy poziom często wskazuje na zanieczyszczenie i potencjał niepożądanego wzrostu biologicznego. Na DOC może również wpływać gęstość innych rozpuszczonych substancji, tj. metale. Poziom materii organicznej w rzece jest ściśle powiązany z opadami/odpływami, porami roku i zazwyczaj waha się w granicach od 0.1 mg L<sup>-1</sup> do 10-20 mg L<sup>-1</sup> w wodach słodkich
(Volk i in. 2022).</p>""", unsafe_allow_html=True)
st.latex(r'''DOC = 432 \cdot \exp\left(-2.24 \cdot \frac{Green}{Red}\right) = 432 \cdot \exp\left(-2.24 \cdot \frac{B3}{B4}\right)''')
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-2"><b>Cyanobacteria</b></span> - wartości tego parametru związane są przede wszystkim z obecnością zakwitów sinic, które mogą być bardzo niebezpieczne dla ludzi, zwierząt i roślin (Topp i in. 2020). Ich zakwity obniżają walory estetyczne rekreacyjnych części zbiorników wodnych. Ponadto, sinice mogą wytwarzać peptydy hepatotoksyczne, tj. Microcystis or Cyanopeptolin, które powodują uszkodzenie wątroby oraz choroby nowotworowe (Hannson i in. 2007). Poniższy wzór został przekształcony na potrzeby Sentinel-2 na podstawie algorytmów stworzonych przez Potesa i in. (2011, 2012).</p>""", unsafe_allow_html=True)
st.latex(r'''Cyanobacteria = 115530.31 \cdot \left(\frac{Green \cdot Red}{Blue}\right)^{2.38} = 115530.31 \cdot \left(\frac{B3 \cdot B4}{B2}\right)^{2.38}''')
st.divider()

st.markdown("""<p class="align-text"> <span class="index-font-2"><b>Turbidity</b></span> - to zmiejszczenie przejrzystości wody na skutek obecności zawiesin pochłaniających lub rozpraszających światło. Poza wpływem na jakość wizualną rzek i zbiorników rekreacyjnych, przezroczystość wody wpływa na zmiany w ilości światła dochodzącego do różnych głębokości, co wpływa na proces fotosyntezy (Izagirre i in. 2009). Poniższy wzór został przekształcony na potrzeby Sentinel-2 na podstawie algorytmów stworzonych przez Potesa i in. (2011, 2012).</p>""", unsafe_allow_html=True)
st.latex(r'''Turbidity = 8.93 \cdot \left(\frac{Green}{Ultra Blue}\right) - 6.39 = 8.93 \cdot \left(\frac{B3}{B1}\right) - 6.39''')
st.divider()

st.header("\n")
st.subheader("References:")
st.markdown("""
            <ul>
              <li>Alawadi F. 2010. <i>"Detection of surface algal blooms using the newly developed algorithm surface algal bloom index (SABI)."</i>, Proc. SPIE 7825, Remote Sensing of the Ocean, Sea Ice, and Large Water Regions 2010, 782506 (18 October 2010). doi:10.1117/12.862096. </li>
              <li>Caballero I., Fernández R., Escalante O.M., Maman L., Navarro G. 2020. <i>"New capabilities of Sentinel-2A/B satellites combined with in situ data for monitoring small harmful algal blooms in complex coastal waters."</i>, Sci Rep 10, 8743. doi:10.1038/s41598-020-65600-1.</li>
              <li>Clarke D., Williams S., Jahiruddin M., Parks K. Salehin M. 2015. <i>"Projections of on-farm salinity in coastal Bangladesh."</i>, Environmental Science: Processes & Impacts. doi:10.1039/C4EM00682H.</li>
              <li>El-Shikha D.M., Waller P., Hunsaker D., Clarke T., Barnes E. 2007. <i>"Ground-based remote sensing for assessing water and nitrogen status of broccoli."</i>, Agriculture water management, 92, pp. 183-193. doi:10.1016/j.agwat.2007.05.020.</li>
              <li>Fichot C.G., Downing B.D., Bergamaschi B.A., Windham-Myers L., Marvin-DiPasquale M., Thompson D.R., Gierach M.M. 2016. <i>"High-Resolution Remote Sensing of Water Quality in the SanFrancisco Bay−Delta Estuary."</i>, Environmental Science and Technology. 50. doi:10.1021/acs.est.5b03518.</li>
              <li>Google Earth Engine (Data Catalog) 2023. <i>"Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-2A."</i> Last modified November 2023. https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED.</li>
              <li>Hannson L.A., Gustafsson S., Rengefors K., Bomark L. 2007. <i>"Cyanobacterial chemical warfare affects zooplankton community composition."</i>, Freshwater Biology. 52. 1290-1301. doi:10.1111/j.1365-2427.2007.01765.x.</li>
              <li>Izagirre O., Serra A., Guasch H., Elosegi A. 2009. <i>"Effects of sediment deposition on periphytic biomass, photosynthetic activity and algal community structure."</i>, Science of The Total Environment, Vol. 407 Issue 21, 5694-5700. doi:10.1016/j.scitotenv.2009.06.049.</li>
              <li>Kulawiak M. 2016. <i>"Operational algae bloom detection in the Baltic Sea using GIS and AVHRR data."</i>, BALTICA. Vol. 29 Issue 1, 3-18. doi:10.5200/baltica.2016.29.02.</li>
              <li>Mahmuduzzaman Md., Uddin Z., Nuruzzaman A.K.M., Rabbi F. 2014. <i>"Causes of Salinity Intrusion in Coastal Belt of Bangladesh."</i>, International Journal of Plant Research, 4(4A), 8-13. doi:10.5923/s.plant.201401.02.</li>
              <li>McFeeters S.K. 1996. <i>"The Use of the Normalized Difference Water Index (NDWI) in the Delineation of Open Water Features."</i>, International Journal of Remote Sensing, 17, 1425-1432. doi:10.1080/01431169608948714.</li>
              <li>Meera Gandhi G., Parthiban S., Thummalu N., Christy A. 2015. <i>"Ndvi: Vegetation Change Detection Using Remote Sensing and Gis – A Case Study of Vellore District."</i>, Procedia Computer Science, Vol. 57, 1199-1210. doi:10.1016.j.procs.2015.07.415.</li>
              <li>Potes M., Costa M.J., da Silva J.C.B., Silva A.M., Morais M. 2011. <i>"Remote sensing of water quality parameters over Alqueva Reservoir in the south of Portugal."</i>, International Journal of Remote Sensing, Vol. 32 Issue 12, 3373-3388. doi:10.1080/01431161003747513.</li>
              <li>Potes M., Costa J., Salgado R. 2012. <i>"Satellite remote sensing of water turbidity in Alqueva reservoir and implications on lake modelling."</i>, Hydrol. Earth Syst. Sci., 16, 1623–1633. doi:10.5194/hess-16-1623-2012.</li>
              <li>Topp M.S., Gokbuget N., Zugmaier G., Stein A.S., Dombret H., Chen Y., Ribera J., Bargou R.C., Horst H., Kantarjian H.M. 2020. <i>"Long-term survival of patients with relapsed/refractory acute lymphoblastic leukemia treated with blinatumomab.", Cancer, Vol. 127 Issue 4, 554-559. doi:10.1002/cncr.33298.</li>
              <li>Volk C., Wood L., Johnson B., Robinson J., Wei Zhu H., Kaplan L. 2002. <i>"Monitoring dissolved organic carbon in surface and drinking waters."</i>, Journal of Environmental Monitoring, 4, 43-47. doi:10.1039/B107768F.</li>
              <li>Yamaguchi T., Kishida K., Nunohiro E., Park JG., Mackin K.J., Matsushita K.H.K., Harada I. 2010. <i>"Artificial neural network paddy-field classifier using Spatiotemporal remote sensing data."</i>, Artificial life and robotics, 15 (2), 221-224. doi:10.1007/s10015-010-0797-4.</li>
              <li>Yang Y., Zhu J., Zhao C., Liu S., Tong X. 2010. <i>"The spatial continuity study of NDVI based on Kriging and BPNN algorithm."</i>, Mathematical and Computer Modelling, Vol. 54 Issues 3-4, 1138-1144. doi:10.1016/j.mcm.2010.11.046.</li>
              <li>Zhang X., Hu Y., Zhuang D., Oi Y., Ma X. 2009. <i>"NDVI spatial pattern and its differentiation on the Mongolian Plateau."</i>, Journal of Geographical Sciences, 19, 403-415. doi:10.1007/s11442-009-0403-7.</li>
            </ul>""", unsafe_allow_html=True)
