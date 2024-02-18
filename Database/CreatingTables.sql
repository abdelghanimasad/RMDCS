CREATE TABLE Street (
  StreetID	 VARCHAR(9) 	NOT NULL,
  StreetName  VARCHAR(50) 	NOT NULL,
  
  PRIMARY KEY (StreetID),
  UNIQUE(StreetName) );


CREATE TABLE electricityconsumption (
		ConsumptionID	VARCHAR(9)	NOT NULL,
        StreetID	VARCHAR(9) 	NOT NULL,
        StartTIme	TIME	NOT NULL,
        EndTime	 TIME 	NOT NULL,
        ElectricityConsumption 	FLOAT(6) 	NOT NULL,
        LightIntensity 	INT(6) 	NOT NULL,
        NumOfCars 	INT(6)	NOT NULL,
        New_ElectricityConsumption 	FLOAT(6),
        New_LightIntensity 	INT(6),
        
        PRIMARY KEY (ConsumptionID),
        FOREIGN KEY (StreetID) REFERENCES Street(StreetID) );

