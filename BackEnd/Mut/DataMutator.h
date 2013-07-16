/* 
 * File:   DataMutator.h
 * Author: golovin
 *
 * Created on 16 Июль 2013 г., 11:58
 */

#ifndef DATAMUTATOR_H
#define	DATAMUTATOR_H

class DataMutator {
public:
    DataMutator();
    
    virtual ~DataMutator();
    
    int mutateInt32(int _value, int _numberOfMutations);
private:

};

#endif	/* DATAMUTATOR_H */

