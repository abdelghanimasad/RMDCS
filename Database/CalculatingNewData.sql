SET SQL_SAFE_UPDATES = 0; -- We do this to remove sql safety in order to update all the tuples

UPDATE ElectricityConsumption
SET New_LightIntensity = 
  CASE 
    WHEN LightIntensity = 0 THEN 0
    WHEN NumOfCars > 50 THEN 100
    WHEN NumOfCars >= 20 AND NumOfCars <= 50 THEN 90
    WHEN NumOfCars >= 10 AND NumOfCars < 20 THEN 80
    WHEN NumOfCars >= 5 AND NumOfCars < 10 THEN 70
    WHEN NumOfCars >= 1 AND NumOfCars < 5 THEN 60
    WHEN NumOfCars = 0 THEN 0
    ELSE 100
  END;

UPDATE ElectricityConsumption
SET New_ElectricityConsumption = ROUND(ElectricityConsumption * (New_LightIntensity / 100.0), 3);