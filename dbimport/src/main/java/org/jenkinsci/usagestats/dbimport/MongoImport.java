package org.jenkinsci.usagestats.dbimport;

import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.List;

import org.codehaus.jackson.JsonNode;

import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBObject;
import com.mongodb.MongoClient;
import com.mongodb.util.JSON;

public class MongoImport {
    
    public static final String DEFAULT_HOSTNAME = "localhost";
    public static final int DEFAULT_PORT = 27017;
    public static final String DEFAULT_DB_NAME = "jenkins_stats";
    public static final String DEFAULT_COLL_NAME = "jstats";
    
    private final DBCollection collection;
    
    public MongoImport() throws UnknownHostException {
        this(DEFAULT_HOSTNAME, DEFAULT_DB_NAME);
    }
    
    public MongoImport(String dbName) throws UnknownHostException {
        this(DEFAULT_HOSTNAME, dbName);
    }
    
    public MongoImport(String host, String dbName) throws UnknownHostException {
        DB db = connect(host, dbName);
        this.collection = db.getCollection(DEFAULT_COLL_NAME);
    }
    
    public DB connect(String host, String dbName) throws UnknownHostException {
        MongoClient mongo = new MongoClient(host, DEFAULT_PORT);
        DB db = mongo.getDB(dbName);
        return db;
    }
    
    public void insertItem(JsonNode node) {
        DBObject dbItem = (DBObject)JSON.parse(node.toString());
        collection.insert(dbItem);
    }
    
    public void insertItems(List<JsonNode> nodes) {
        List<DBObject> dbItems = new ArrayList<DBObject>();
        for(JsonNode node : nodes) 
            dbItems.add((DBObject)JSON.parse(node.toString()));
        collection.insert(dbItems);
    }

}
