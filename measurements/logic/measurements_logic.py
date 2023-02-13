from ..models import Measurement
from variables import models
from variables.models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(meas_pk):
    measurement = Measurement.objects.get(pk=meas_pk)
    return measurement

def create_measurement(meas):
    variable_pk = Variable.objects.get(pk=meas["variable"])
    measurement = Measurement(variable= variables_pk,value=meas["value"],unit=meas["unit"],place=meas["place"],dateTime=meas["dateTime"])
    measurement.save()
    return measurement

def update_measurement(meas_pk, new_meas):
    measurement = get_measurement(meas_pk)
    measurement.value = new_meas["value"]
    measurement.unit = new_meas["unit"]
    measurement.place = new_meas["place"]
    measurement.dateTime = new_meas["dateTime"]

    measurement.save()
    return measurement

def delete_measurement(meas_pk):
    measurement = get_measurement(meas_pk) 
    measurement.delete
    measurement.save()
    return measurement
