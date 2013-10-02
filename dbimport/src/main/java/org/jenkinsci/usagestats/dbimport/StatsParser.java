package org.jenkinsci.usagestats.dbimport;

import java.io.File;
import java.io.IOException;

import org.codehaus.jackson.JsonNode;
import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.JsonParser;
import org.codehaus.jackson.JsonToken;
import org.codehaus.jackson.map.MappingJsonFactory;

public class StatsParser {

    private final JsonParser parser;
    private JsonToken token;
    
    public StatsParser(File jsonFile) throws IOException, JsonParseException {
        parser = (new MappingJsonFactory()).createJsonParser(jsonFile);
        init();
    }
    
    private void init() throws IOException, JsonParseException {
        token = parser.nextToken();
      //TODO check start element
    }
    
    public JsonNode getNextNode() throws IOException, JsonParseException {
        if(parser.nextToken() == JsonToken.END_OBJECT)
            return null;
        
        JsonNode node = null;
        token = parser.nextToken();
        if (token == JsonToken.START_ARRAY) {
            //iterate over array and return last one
            //TODO add all and filet on DB level
            while (parser.nextToken() != JsonToken.END_ARRAY) {
                node = parser.readValueAsTree();
            }
        } else {
            parser.skipChildren();
            node = getNextNode();
        }
        
        return node;
    }
    
}
