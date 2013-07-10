#include "jsonparse.h"

int jsonParse(string _s)
{
    // Let's parse it  
    Json::Value root;
    Json::Reader reader;
    bool parsedSuccess = reader.parse(_s,
            root,
            false);

    if (not parsedSuccess) {
        // Report failures and their locations 
        // in the document.
        cout << "Failed to parse JSON" << endl
                << reader.getFormatedErrorMessages()
                << endl;
        return 1;
    }
    
    Json::Value::Members mem = root.getMemberNames();
    Json::Value child = root[mem[0]];
    cout << "name: " << mem[0] << ", child: " << child.asString() << endl;
    for (int i = 1; i < mem.size(); ++i)
    {
        child = root[mem[i]];
        cout << "name: " << mem[i] << endl;
        Json::Value::Members childMem = child.getMemberNames();
        cout << "\t" << "type: " << child[childMem[0]].asString() << endl;
        cout << "\t" << "value: " << child[childMem[1]].asString() << endl;
        cout << "\t" << "typeGen: " << child[childMem[2]].asString() << endl;
    }
    return 1;
}

