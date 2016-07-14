import java.io.File;
 
import org.w3c.dom.*;
 
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException; 
 
import java.io.BufferedWriter;
import java.io.FileWriter;
 
/**
*  This program extracts relevant data from the NDV data feeds for generating mappings:
*   :: "ITProduct - CVEID" -> *.txt 
*   :: And any other mappings you may desire.
*/
 
public class ITProductCVEID{
 
    public static void main (String argv []){
    try {
            File file = new File("../../coreFiles/ITProduct-CVEID.txt");
         
            // if file doesn't exists, then create it
            if (!file.exists()) {
                file.createNewFile();
            }
             
            FileWriter fw = new FileWriter(file.getAbsoluteFile());
            BufferedWriter bw = new BufferedWriter(fw);
             
            String content = " ";
             
            DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
             
            // Add a for loop to iterate through all NVD databases feeds at once
            int year = 2002;
            String urlNVDFeed = "";
             
            for(int theYear=year; theYear<=2016 ; theYear++){
                
                urlNVDFeed = "../../Data-Feeds/NVD/nvdcve-2.0-"+ theYear + ".xml" ;
                 
                Document doc = docBuilder.parse (new File(urlNVDFeed)); 
     
                // normalize text representation
                doc.getDocumentElement ().normalize ();
                System.out.println ("Root element of the doc is " + 
                     doc.getDocumentElement().getNodeName());
     
     
                NodeList listOfCVEs = doc.getElementsByTagName("entry");
                 
                int totalPersons = listOfCVEs.getLength();
                System.out.println("Total no of CVE-IDs : " + totalPersons);
     
                Element firstCVEElement;
                int i;   
                NodeList entries;
                //NodeList subEntries;
                 
                String itProd   = ""; // To store temporally extracted IT products
                String cve_ID   = ""; // To store temporally extracted CVE-ID
                String summary  = ""; // To store temporally extracted Summaries
                String cvssMets = ""; // To store the list of CVSS metrics to be factored into individual ones.
                 
                for(int s=0; s<listOfCVEs.getLength() ; s++){
     
                     
                       firstCVEElement = (Element) listOfCVEs.item(s);                   
                       System.out.println(firstCVEElement.getTagName() + ":");                   
                       entries = firstCVEElement.getChildNodes();                                     
                        
                       if (entries != null){
                           for (i=0; i < entries.getLength(); i++)
                           {                           
                               if (entries.item(i).getNodeName().toString() == "vuln:vulnerable-software-list"){
                                   itProd = entries.item(i).getTextContent();
                               }                           
                                
                               if (entries.item(i).getNodeName().toString() == "vuln:cve-id"){
                                   cve_ID = entries.item(i).getTextContent();
                               }
                                
                               if (entries.item(i).getNodeName().toString() == "vuln:cvss"){
                                   cvssMets =entries.item(i).getTextContent();               
                               }
                                
                               if (entries.item(i).getNodeName().toString() == "vuln:summary"){
                                   summary = entries.item(i).getTextContent();
                               }                   
                           }  
                            
                           // Now let's split each individual metrics separated by '\n'                  
                            
                           String delims = "[\n]+";
                           String[] tokens = cvssMets.split(delims);   
                            
                           String score = tokens[2];                       
                           String accessVector = tokens[3];
                           String accessComplexity = tokens[4];
                           String authentication = tokens[5];
                           String confidentialityImpact = tokens[6];
                           String integrityImpact = tokens[7];
                           String availabilityImpact = tokens[8];
                            
                           // IT Products
                           System.out.println(itProd);
                            
                           // CVE-ID
                           System.out.println(cve_ID);
                            
                           //CVSS Metrics         
                           System.out.println(score);
                           System.out.println(accessVector);
                           System.out.println(accessComplexity);
                           System.out.println(authentication);
                           System.out.println(confidentialityImpact);
                           System.out.println(integrityImpact);
                           System.out.println(availabilityImpact);
                            
                           // Summary                  
                           System.out.println(summary);     
                            
                           String[] prods = itProd.split(delims);

                           for(int v=1; v < (prods.length - 1) ; v++){
                                
                               content = prods[v] + "&" + cve_ID + "\n";
                               bw.write(content);
                               content = "";
                                
                           }
                             
                       }
     
                }//end of for loop with s var
            }
            bw.close();
            System.out.println("\n\nDone\n\n");

        }catch (SAXParseException err) {
        System.out.println ("** Parsing error" + ", line "
             + err.getLineNumber () + ", uri " + err.getSystemId ());
        System.out.println(" " + err.getMessage ());
 
        }catch (SAXException e) {
        Exception x = e.getException ();
        ((x == null) ? e : x).printStackTrace ();
 
        }catch (Throwable t) {
        t.printStackTrace ();
        }
        //System.exit (0);
 
    }//end of main
}