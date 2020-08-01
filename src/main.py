import xml.etree.ElementTree as ET


class Word:
    """base structure of parsed words, gets committed to XML file"""

    def __init__(self, norm, dipl, fak, lemma, gram, lang, ref, doc):
        self.dipl = dipl
        self.norm = norm
        self.fak = fak
        self.lemma = lemma
        self.gram = gram
        self.lang = lang
        self.ref = ref
        self.doc = doc

    'creates XML file for each word with SubElements which house the attributes of the obj'

    def committoxml(self):
        wordXML = ET.Element('word')
        normXML = ET.SubElement(wordXML, 'norm')
        diplXML = ET.SubElement(wordXML, 'dipl')
        fakXML = ET.SubElement(wordXML, 'fak')
        lemmaXML = ET.SubElement(wordXML, 'lemma')
        gramXML = ET.SubElement(wordXML, 'gram')
        langXML = ET.SubElement(wordXML, 'lang')
        refXML = ET.SubElement(wordXML, 'ref')
        docXML = ET.SubElement(wordXML, 'doc')
        normXML.set('name', 'norm')
        normXML.text = self.norm
        diplXML.set('name', 'dipl')
        diplXML.text = self.dipl
        fakXML.set('name', 'fak')
        fakXML.text = self.fak
        lemmaXML.set('name', 'lemma')
        lemmaXML.text = self.lemma
        gramXML.set('name', 'gram')
        gramXML.text = self.gram
        langXML.set('name', 'lang')
        langXML.text = self.lang
        refXML.set('name', 'ref')
        refXML.text = self.ref
        docXML.set('name', 'doc')
        docXML.text = self.doc

        output1 = ""
        output1 = ET.tostring(wordXML, "utf-8", "xml")
        output1 = str(output1)
        outputfile = open("word.xml", "w")
        outputfile.write(output1)


word1 = Word("hann", "han", "h_", "hann", "xPE p3 gM nS cN", "oic", "26r 13", "Wolf-Aug-9-10-4to")
word1.committoxml()
print("Success!")
