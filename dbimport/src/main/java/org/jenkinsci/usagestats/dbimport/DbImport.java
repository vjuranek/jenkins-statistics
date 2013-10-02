package org.jenkinsci.usagestats.dbimport;

import java.io.File;

import org.codehaus.jackson.JsonNode;

public class DbImport {
    
    public static void main(String[] args) throws Exception {
        File f = new File(args[0]);
        DbImport importer = new DbImport();        
        int imported = importer.pushToMongo(f);
        System.out.println(String.format("Imported %d items", imported));
    }
    
    public int pushToMongo(File jsonFile) throws Exception {
        StatsParser parser = new StatsParser(jsonFile);
        MongoImport mongoImport = new MongoImport();
        JsonNode node = parser.getNextNode();
        int i = 0;
        while(node != null) {
            mongoImport.insertItem(node);
            node = parser.getNextNode();
            i++;
        }
        return i;
    }

}