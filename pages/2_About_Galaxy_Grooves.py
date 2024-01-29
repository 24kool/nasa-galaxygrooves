import streamlit as st

st.set_page_config(page_title="About GalaxyGrooves", page_icon="🎶")

header = ("# Enjoyed listening to Galaxy Groove?  \n"
          "Here's the methodology behind how we created those *galactic* sounds!")
st.markdown(header)



st.header("WISE: Our Data Source", divider='orange')
st.markdown("We used data recorded by NASA's Wide-field Infrared Survey Explorer (WISE).  \n"
            "The WISE telescope measures 4 different types of wavelength bands: 3.4, 4.6, 12, and 22μm wavelength range bands.  \n"
            "Each band wavelength corresponds to a range of thermal activity.  \n"
            "For example,  \n"
            "- Band 1 (3.4μm): Broad-band sensitivity to stars and galaxies  \n"
            "- Band 2 (4.6μm): Sub-stellar objects such as brown dwarfs  \n"
            "- Band 3 (12μm): Detects thermal radiation from asteroids  \n"
            "- Band 4 (22μm): Sensitivity to dust in star-forming regions  \n"
            "[Source](https://en.wikipedia.org/wiki/Wide-field_Infrared_Survey_Explorer)")

st.header("Our Sonification Process", divider='orange')
st.markdown("From one image, we first begin the process by forming subsections of 10 x 10 pixels and averaging the "
            "RGB values to determine the averaged RGB value for this subsection."
            " Then, we perform a second calculation to average the R,G,B values to compute a decimal number. "
            "We use this decimal number as one parameter for our audio generator function.")

st.markdown("#### Band 1: The Pitch  \n"
            "We use Band 1 as the source data to determine our pitch. The location of the celestial object determines"
            "the range for our pitch. We use the right ascension and declination values of the celestial object to delineate"
            " the upper maximum frequency and the declination to delineate the lower minimum frequency.")

st.markdown("#### Band 2: The Length  \n"
            "We use Band 2 as the source data to determine the length of each note. The greater the intensity of the "
            "subsection image, the longer our note.")

st.markdown("#### Band 4: The Volume  \n"
            "We use Band 4 as the source data to determine the volume of each note. The higher concentration of "
            "dust, our note will be louder.")