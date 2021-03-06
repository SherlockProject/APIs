from REST.API import SherlockAPI


# Concept Expansion Service
concexp = SherlockAPI(
    # Service URL
    url = 'https://gateway.watsonplatform.net/concept-expansion-beta/api',
    # Credentails (User, Pass)
    auth = ( 'bf269ea5-03c4-4cbf-8ca6-04a2a4ea1e03', '93NpKVPd9sxA' ),
    # REST API Services
    operations = {
        'ping': {
            'method' : 'GET',
            'path' : '/v1/ping'
        },
        'upload': {
            'method': 'POST',
            'path': '/v1/upload'
        },
        'status': {
            'method': 'GET',
            'path': '/v1/status'
        },
        'result': {
            'method': 'PUT',
            'path': '/v1/result'
        }

    } );


relaextrac = SherlockAPI(
    # Service URL
    url = "https://gateway.watsonplatform.net/relationship-extraction-beta/api",
    # Credentails (User, Pass)
    auth = ( 'c3ddb65d-8196-4022-9db7-f066196b5fe5', 'PIyELwgApv1G' ),
    # REST API Services
    operations = {
        'extract': {
            'method':   'POST',
            'path':     '/v1/sire/0'
        }
    } );


def test_concept_expansion():
    response = concexp.ping()
    print('Available:', response)

    response = concexp.status()
    print('Status', response, type(response))

    print()
    params = {
        'seeds' : seeds,
        'dataset' : 'mtsamples',
        'label' : 'eye-infection'
    }
    response = concexp.upload(params=params)
    print('Seed', response)

    print()
    response = concexp.status()
    print('Status', response)

    print()
    response = concexp.result()
    print('result', response)


def test_relation_extraction():
    sid = 'en'
    txt = """
Microwaves are a form of electromagnetic radiation with wavelengths ranging from as long as one meter to as short as one millimeter; with frequencies between 300 MHz (100 cm) and 300 GHz (0.1 cm).[1][2] This broad definition includes both UHF and EHF (millimeter waves), and various sources use different boundaries. In all cases, microwave includes the entire SHF band (3 to 30 GHz, or 10 to 1 cm) at minimum, with RF engineering often restricting the range between 1 and 100 GHz (300 and 3 mm).

The prefix micro- in microwave is not meant to suggest a wavelength in the micrometer range. It indicates that microwaves are "small", compared to waves used in typical radio broadcasting, in that they have shorter wavelengths. The boundaries between far infrared, terahertz radiation, microwaves, and ultra-high-frequency radio waves are fairly arbitrary and are used variously between different fields of study.

Beginning at about 40 GHz, the atmosphere becomes less transparent to microwaves, due at lower frequencies to absorption from water vapor and at higher frequencies from oxygen. A spectral band structure causes absorption peaks at specific frequencies (see graph at right). Above 100 GHz, the absorption of electromagnetic radiation by Earth's atmosphere is so great that it is in effect opaque, until the atmosphere becomes transparent again in the so-called infrared and optical window frequency ranges.

The term microwave also has a more technical meaning in electromagnetics and circuit theory. Apparatus and techniques may be described qualitatively as "microwave" when the frequencies used are high enough that wavelengths of signals are roughly the same as the dimensions of the equipment, so that lumped-element circuit theory is inaccurate. As a consequence, practical microwave technique tends to move away from the discrete resistors, capacitors, and inductors used with lower-frequency radio waves. Instead, distributed circuit elements and transmission-line theory are more useful methods for design and analysis. Open-wire and coaxial transmission lines used at lower frequencies are replaced by waveguides and stripline, and lumped-element tuned circuits are replaced by cavity resonators or resonant lines. In turn, at even higher frequencies, where the wavelength of the electromagnetic waves becomes small in comparison to the size of the structures used to process them, microwave techniques become inadequate, and the methods of optics are used.
"""
    rt = 'json'
    response = relaextrac.extract(sid, txt, rt)
    print('Response:',response)

if __name__=='__main__' :
    test_relation_extraction()
