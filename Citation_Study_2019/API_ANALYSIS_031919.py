import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

API_results = pd.read_csv("API_results_CLEANED_10.csv")
list(API_results.columns.values)

API_results['Highlight'] = API_results['Highlight'].astype('|S')

#_____________________TARDIS____________________________________
# emails
API_results = API_results[~API_results.Highlight.str.contains("@<em>tardis</em>")]
API_results = API_results[~API_results.Highlight.str.contains("@tardis.byu.edu")]
API_results = API_results[~API_results.Highlight.str.contains("@tardis.ln.byu.edu")]
API_results = API_results[~API_results.Highlight.str.contains("@tardis.pha.jhu.edu")]
API_results = API_results[~API_results.Highlight.str.contains("tardis.ln.byu.edu")]

# detector
API_results = API_results[~(API_results.Highlight.str.contains("detector") & API_results.Software_Package.str.contains("TARDIS"))]
API_results = API_results[~(API_results.Highlight.str.contains("Detector") & API_results.Software_Package.str.contains("TARDIS"))]
API_results = API_results[~(API_results.Highlight.str.contains("bubble") & API_results.Software_Package.str.contains("TARDIS"))]
API_results = API_results[~(API_results.Highlight.str.contains("travel") & API_results.Software_Package.str.contains("TARDIS"))]
API_results = API_results[~(API_results.Highlight.str.contains("boundaries") & API_results.Software_Package.str.contains("TARDIS"))]
API_results = API_results[~(API_results.Highlight.str.contains("triangulations") & API_results.Software_Package.str.contains("TARDIS"))]

# detection
API_results = API_results[~(API_results.Highlight.str.contains("detection") & API_results.Software_Package.str.contains("TARDIS"))]
API_results = API_results[~(API_results.Highlight.str.contains("Detection") & API_results.Software_Package.str.contains("TARDIS"))]

# stardisk
API_results = API_results[~(API_results.Highlight.str.contains("stardisk") & API_results.Software_Package.str.contains("TARDIS"))]
API_results = API_results[~(API_results.Highlight.str.contains("STARDISK") & API_results.Software_Package.str.contains("TARDIS"))]
API_results = API_results[~(API_results.Highlight.str.contains("Stardisk") & API_results.Software_Package.str.contains("TARDIS"))]

#_____________________Stingray____________________________________

# stingray nebula
API_results = API_results[~(API_results.Highlight.str.contains("Nebula") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("nebula") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("CCD") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("ccd") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("camera") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("leather") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("detector") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("fish") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("shark") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("shaped") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("marine") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("lens") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("biology") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("optics") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("Optics") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("tuna") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("bay") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("Bay") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("reef") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("laser") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("robot") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("wing") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("wings") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("Corvette") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("water") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("swimming") & API_results.Software_Package.str.contains("Stingray"))]

# the stingray
API_results = API_results[~(API_results.Highlight.str.contains("The Stingray") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("The stingray") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("the stingray") & API_results.Software_Package.str.contains("Stingray"))]

# stingray light curve
API_results = API_results[~(API_results.Highlight.str.contains("Stingray Light Curve") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("Stingray light curve") & API_results.Software_Package.str.contains("Stingray"))]
API_results = API_results[~(API_results.Highlight.str.contains("stingray light curve") & API_results.Software_Package.str.contains("Stingray"))]

#_____________________Spec2d____________________________________

# IDL
API_results = API_results[~(API_results.Highlight.str.contains("idlspec2d") & API_results.Software_Package.str.contains("Spec2d"))]
API_results = API_results[~(API_results.Highlight.str.contains("IDLspec2d") & API_results.Software_Package.str.contains("Spec2d"))]

#_____________________citation_finder_________________________

citation_finder = API_results.Highlight.str.find('(') != -1

API_results['Citation'] = citation_finder

API_results.to_csv("API_results_CLEANED_11.csv")

print('CSV saved')