# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AccessLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.CharField(unique=True, max_length=60)
    german = models.CharField(max_length=60, db_column='German', blank=True) # Field name made lowercase.
    dutch = models.CharField(max_length=60, db_column='Dutch', blank=True) # Field name made lowercase.
    french = models.CharField(max_length=60, db_column='French', blank=True) # Field name made lowercase.
    italian = models.CharField(max_length=60, db_column='Italian', blank=True) # Field name made lowercase.
    english = models.CharField(max_length=60, db_column='English', blank=True) # Field name made lowercase.
    russisch = models.CharField(max_length=60, db_column='Russisch', blank=True) # Field name made lowercase.
    
    def __unicode__(self):
        return "#%s: %s" % (self.id, self.level)

    class Meta:
        db_table = u'access_level'


class ActualData(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    modulid = models.ForeignKey('Modul', db_column='ModulID') # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp') # Field name made lowercase.
    evtype = models.IntegerField(null=True, db_column='EvType', blank=True) # Field name made lowercase.
    evtime = models.DateTimeField(db_column='EvTime') # Field name made lowercase.
    devicestatus = models.IntegerField(null=True, db_column='DeviceStatus', blank=True) # Field name made lowercase.
    postime = models.DateTimeField(db_column='PosTime') # Field name made lowercase.
    poslat = models.FloatField(null=True, db_column='PosLat', blank=True) # Field name made lowercase.
    poslon = models.FloatField(null=True, db_column='PosLon', blank=True) # Field name made lowercase.
    posalt = models.IntegerField(null=True, db_column='PosAlt', blank=True) # Field name made lowercase.
    posspeed = models.IntegerField(null=True, db_column='PosSpeed', blank=True) # Field name made lowercase.
    posdir = models.IntegerField(null=True, db_column='PosDir', blank=True) # Field name made lowercase.
    possat = models.IntegerField(null=True, db_column='PosSat', blank=True) # Field name made lowercase.
    zone = models.IntegerField(null=True, db_column='Zone', blank=True) # Field name made lowercase.
    reversegeodataid = models.ForeignKey('ReverseData', null=True, db_column='ReverseGeoDataID', blank=True) # Field name made lowercase.
    comtechnology = models.CharField(max_length=30, db_column='ComTechnology', blank=True) # Field name made lowercase.
    previd = models.IntegerField(null=True, db_column='PrevID', blank=True) # Field name made lowercase.

    def __unicode__(self):
        return "#%s: %s" % (self.id, self.modulid)

    class Meta:
        db_table = u'actual_data'
        verbose_name_plural = u'Actual Data'

class ActualDataAnalog(models.Model):
    id = models.IntegerField(primary_key=True)
    actualdataid = models.IntegerField(db_column='ActualDataID') # Field name made lowercase.
    dieselfuellstand = models.FloatField(null=True, db_column='Dieselfuellstand', blank=True) # Field name made lowercase.
    raumtempwagen = models.FloatField(null=True, db_column='RaumtempWagen', blank=True) # Field name made lowercase.
    tempaggregat = models.FloatField(null=True, db_column='TempAggregat', blank=True) # Field name made lowercase.
    tempictschrank1 = models.FloatField(null=True, db_column='TempICTSchrank1', blank=True) # Field name made lowercase.
    tempictschrank2 = models.FloatField(null=True, db_column='TempICTSchrank2', blank=True) # Field name made lowercase.
    battspwagen = models.FloatField(null=True, db_column='BattspWagen', blank=True) # Field name made lowercase.
    battspaggregat = models.FloatField(null=True, db_column='BattspAggregat', blank=True) # Field name made lowercase.
    hbldruck = models.FloatField(null=True, db_column='HBLDruck', blank=True) # Field name made lowercase.
    hlldruck = models.FloatField(null=True, db_column='HLLDruck', blank=True) # Field name made lowercase.
    timestamputc = models.DateTimeField(null=True, db_column='TimestampUTC', blank=True) # Field name made lowercase.

    def __unicode__(self):
            return "#%s: %s" % (self.id, self.actualdataid)

    class Meta:
        db_table = u'actual_data_analog'
        verbose_name_plural = u'Actual Data Analog'

class ActualDataDigital(models.Model):
    id = models.IntegerField(primary_key=True)
    actualdataid = models.IntegerField(db_column='ActualDataID') # Field name made lowercase.
    schuppenstecker = models.IntegerField(null=True, db_column='Schuppenstecker', blank=True) # Field name made lowercase.
    zss = models.IntegerField(null=True, db_column='ZSS', blank=True) # Field name made lowercase.
    diesel = models.IntegerField(null=True, db_column='Diesel', blank=True) # Field name made lowercase.
    brandmeldestoerg = models.IntegerField(null=True, db_column='Brandmeldestoerg', blank=True) # Field name made lowercase.
    brandmeldealarm = models.IntegerField(null=True, db_column='Brandmeldealarm', blank=True) # Field name made lowercase.
    fzgsammelstoerg = models.IntegerField(null=True, db_column='FzgSammelstoerg', blank=True) # Field name made lowercase.
    stoergaggregat = models.IntegerField(null=True, db_column='StoergAggregat', blank=True) # Field name made lowercase.
    notbremse = models.IntegerField(null=True, db_column='Notbremse', blank=True) # Field name made lowercase.
    handbremse = models.IntegerField(null=True, db_column='Handbremse', blank=True) # Field name made lowercase.
    bmaabteil = models.IntegerField(null=True, db_column='BMAAbteil', blank=True) # Field name made lowercase.
    bmazwischendecke = models.IntegerField(null=True, db_column='BMAZwischendecke', blank=True) # Field name made lowercase.
    bmaabluft = models.IntegerField(null=True, db_column='BMAAbluft', blank=True) # Field name made lowercase.
    bmamr = models.IntegerField(null=True, db_column='BMAMR', blank=True) # Field name made lowercase.
    brandmelderdeutz = models.IntegerField(null=True, db_column='BrandmelderDeutz', blank=True) # Field name made lowercase.
    bmaabteil2 = models.IntegerField(null=True, db_column='BMAAbteil2', blank=True) # Field name made lowercase.
    bmazwischendecke2 = models.IntegerField(null=True, db_column='BMAZwischendecke2', blank=True) # Field name made lowercase.
    bmaabluft2 = models.IntegerField(null=True, db_column='BMAAbluft2', blank=True) # Field name made lowercase.
    bmamr2 = models.IntegerField(null=True, db_column='BMAMR2', blank=True) # Field name made lowercase.
    brandmelder1234stoerung = models.IntegerField(null=True, db_column='Brandmelder1234Stoerung', blank=True) # Field name made lowercase.
    brandmelderdeutz2 = models.IntegerField(null=True, db_column='BrandmelderDeutz2', blank=True) # Field name made lowercase.
    dieselstoergtwido = models.IntegerField(null=True, db_column='DieselstoergTwido', blank=True) # Field name made lowercase.
    twidocomok = models.IntegerField(null=True, db_column='TwidoComOK', blank=True) # Field name made lowercase.
    wagendrahtbruch_24v = models.IntegerField(null=True, db_column='24VWagenDrahtbruch', blank=True) # Field name made lowercase.
    hlldrahtbruch = models.IntegerField(null=True, db_column='HLLDrahtbruch', blank=True) # Field name made lowercase.
    hbldrahtbruch = models.IntegerField(null=True, db_column='HBLDrahtbruch', blank=True) # Field name made lowercase.
    dieseldruckdrahtbruch = models.IntegerField(null=True, db_column='DieseldruckDrahtbruch', blank=True) # Field name made lowercase.
    trafotempdrahtbruch = models.IntegerField(null=True, db_column='TrafotempDrahtbruch', blank=True) # Field name made lowercase.
    twidobatlow = models.IntegerField(null=True, db_column='TwidoBatLow', blank=True) # Field name made lowercase.
    wagenbatlow = models.IntegerField(null=True, db_column='WagenBatLow', blank=True) # Field name made lowercase.
    frostalarm = models.IntegerField(null=True, db_column='Frostalarm', blank=True) # Field name made lowercase.
    cpu727comok = models.IntegerField(null=True, db_column='CPU727ComOK', blank=True) # Field name made lowercase.
    timestamputc = models.DateTimeField(null=True, db_column='TimestampUTC', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'actual_data_digital'
        verbose_name_plural = u'Actual Data Digital'

class ActualDataExtend(models.Model):
    actualdataid = models.ForeignKey(ActualData, db_column='ActualDataId') # Field name made lowercase.
    nextstation = models.CharField(max_length=765, db_column='NextStation', blank=True) # Field name made lowercase.
    uicposition = models.CharField(max_length=765, db_column='UICPosition', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'actual_data_extend'

class ActualDataLast(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    actualdataid = models.ForeignKey(ActualData, db_column='ActualDataID') # Field name made lowercase.
    modulid = models.ForeignKey('Modul', db_column='ModulID') # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp') # Field name made lowercase.
    evtype = models.IntegerField(null=True, db_column='EvType', blank=True) # Field name made lowercase.
    evtime = models.DateTimeField(db_column='EvTime') # Field name made lowercase.
    devicestatus = models.IntegerField(null=True, db_column='DeviceStatus', blank=True) # Field name made lowercase.
    postime = models.DateTimeField(db_column='PosTime') # Field name made lowercase.
    poslat = models.FloatField(null=True, db_column='PosLat', blank=True) # Field name made lowercase.
    poslon = models.FloatField(null=True, db_column='PosLon', blank=True) # Field name made lowercase.
    posalt = models.IntegerField(null=True, db_column='PosAlt', blank=True) # Field name made lowercase.
    posspeed = models.IntegerField(null=True, db_column='PosSpeed', blank=True) # Field name made lowercase.
    posdir = models.IntegerField(null=True, db_column='PosDir', blank=True) # Field name made lowercase.
    possat = models.IntegerField(null=True, db_column='PosSat', blank=True) # Field name made lowercase.
    prevevtime = models.IntegerField(db_column='PrevEvTime') # Field name made lowercase.
    class Meta:
        db_table = u'actual_data_last'

class AlertMatrixAnalog(models.Model):
    modulid = models.ForeignKey('Modul', db_column='ModulID') # Field name made lowercase.
    instance = models.IntegerField(primary_key=True, db_column='Instance') # Field name made lowercase.
    minvalue = models.IntegerField(db_column='MinValue') # Field name made lowercase.
    condition = models.CharField(max_length=6, db_column='Condition', blank=True) # Field name made lowercase.
    alertvalue = models.IntegerField(db_column='AlertValue') # Field name made lowercase.
    maxvalue = models.IntegerField(db_column='MaxValue') # Field name made lowercase.
    unit = models.CharField(max_length=15, db_column='Unit', blank=True) # Field name made lowercase.
    lastmodification = models.DateTimeField(null=True, db_column='LastModification', blank=True) # Field name made lowercase.
    lastmodificationby = models.CharField(max_length=60, db_column='LastModificationBy', blank=True) # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'alert_matrix_analog'

class AlertMatrixDigital(models.Model):
    modulid = models.ForeignKey('Modul', db_column='ModulID') # Field name made lowercase.
    instance = models.IntegerField(primary_key=True, db_column='Instance') # Field name made lowercase.
    alertvalue = models.CharField(max_length=12, db_column='AlertValue') # Field name made lowercase.
    lastmodification = models.DateTimeField(null=True, db_column='LastModification', blank=True) # Field name made lowercase.
    lastmodificationby = models.CharField(max_length=60, db_column='LastModificationBy', blank=True) # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'alert_matrix_digital'

class ApplictionObject(models.Model):
    sess = models.CharField(max_length=255, primary_key=True)
    obj = models.CharField(max_length=255, primary_key=True)
    variables = models.TextField()
    class Meta:
        db_table = u'appliction_object'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type_id = models.IntegerField()
    codename = models.CharField(unique=True, max_length=255)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_user_permissions'

class CustomerInfoMsg(models.Model):
    id = models.IntegerField(primary_key=True)
    mandantid = models.IntegerField(db_column='MandantID') # Field name made lowercase.
    infotitle = models.CharField(max_length=60, db_column='Infotitle') # Field name made lowercase.
    customerinfo = models.TextField(db_column='Customerinfo', blank=True) # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True) # Field name made lowercase.
    enabled = models.IntegerField(null=True, db_column='Enabled', blank=True) # Field name made lowercase.
    lastmodification = models.DateTimeField(null=True, db_column='LastModification', blank=True) # Field name made lowercase.
    lastmodificationby = models.CharField(max_length=90, db_column='LastModificationBy', blank=True) # Field name made lowercase.
    dateofcreation = models.DateTimeField(null=True, db_column='DateOfCreation', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'customer_info_msg'

class Debug(models.Model):
    id = models.IntegerField(primary_key=True)
    debug = models.TextField(blank=True)
    class Meta:
        db_table = u'debug'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=255)
    model = models.CharField(unique=True, max_length=255)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class ErrorLog(models.Model):
    id = models.IntegerField(primary_key=True)
    db_name = models.CharField(max_length=60, blank=True)
    proc_name = models.CharField(max_length=108, blank=True)
    error_date = models.DateTimeField(null=True, blank=True)
    code = models.CharField(max_length=21, blank=True)
    message = models.CharField(max_length=240, blank=True)
    user = models.CharField(max_length=240, blank=True)
    class Meta:
        db_table = u'error_log'

class Fleets(models.Model):
    fleetid = models.IntegerField(primary_key=True, db_column='FleetID') # Field name made lowercase.
    mandantid = models.ForeignKey('Mandant', db_column='MandantID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    assignmentcounter = models.IntegerField(db_column='AssignmentCounter') # Field name made lowercase.
    dateofcreation = models.DateTimeField(null=True, db_column='DateOfCreation', blank=True) # Field name made lowercase.
    lastmodification = models.DateTimeField(null=True, db_column='LastModification', blank=True) # Field name made lowercase.
    lastmodificationby = models.CharField(max_length=60, db_column='LastModificationBy', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'fleets'
        verbose_name_plural = u'fleets'

class GisUic(models.Model):
    uic_id = models.IntegerField(primary_key=True)
    uic_code = models.CharField(max_length=30)
    uic_description = models.CharField(max_length=120)
    uic_lat = models.IntegerField()
    uic_lon = models.IntegerField()
    class Meta:
        db_table = u'gis_uic'

class ImportAccessLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.CharField(unique=True, max_length=60)
    german = models.CharField(max_length=60, db_column='German', blank=True) # Field name made lowercase.
    dutch = models.CharField(max_length=60, db_column='Dutch', blank=True) # Field name made lowercase.
    french = models.CharField(max_length=60, db_column='French', blank=True) # Field name made lowercase.
    italian = models.CharField(max_length=60, db_column='Italian', blank=True) # Field name made lowercase.
    english = models.CharField(max_length=60, db_column='English', blank=True) # Field name made lowercase.
    russisch = models.CharField(max_length=60, db_column='Russisch', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'import_access_level'

class ImportLookup(models.Model):
    id = models.IntegerField(primary_key=True)
    klasse = models.CharField(max_length=60)
    code = models.CharField(max_length=60)
    german = models.CharField(max_length=150, db_column='German') # Field name made lowercase.
    dutch = models.CharField(max_length=150, db_column='Dutch') # Field name made lowercase.
    french = models.CharField(max_length=150, db_column='French') # Field name made lowercase.
    italian = models.CharField(max_length=150, db_column='Italian') # Field name made lowercase.
    english = models.CharField(max_length=150, db_column='English') # Field name made lowercase.
    russisch = models.CharField(max_length=150, db_column='Russisch') # Field name made lowercase.
    class Meta:
        db_table = u'import_lookup'

class ImportText(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=150, db_column='Type', blank=True) # Field name made lowercase.
    page = models.CharField(max_length=150, db_column='Page', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name', blank=True) # Field name made lowercase.
    german = models.TextField(db_column='German', blank=True) # Field name made lowercase.
    dutch = models.TextField(db_column='Dutch', blank=True) # Field name made lowercase.
    french = models.TextField(db_column='French', blank=True) # Field name made lowercase.
    italian = models.TextField(db_column='Italian', blank=True) # Field name made lowercase.
    english = models.TextField(db_column='English', blank=True) # Field name made lowercase.
    russisch = models.TextField(db_column='Russisch', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'import_text'

class Log(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    loginname = models.CharField(max_length=60, db_column='Loginname') # Field name made lowercase.
    loginerror = models.CharField(max_length=3, db_column='LoginError', blank=True) # Field name made lowercase.
    loginerrortime = models.DateTimeField(null=True, db_column='LoginErrorTime', blank=True) # Field name made lowercase.
    logintime = models.DateTimeField(null=True, db_column='LoginTime', blank=True) # Field name made lowercase.
    sid = models.CharField(max_length=96, db_column='SID', blank=True) # Field name made lowercase.
    ip = models.CharField(max_length=300, db_column='IP') # Field name made lowercase.
    lastaction = models.DateTimeField(null=True, db_column='LastAction', blank=True) # Field name made lowercase.
    actioncounter = models.IntegerField(null=True, db_column='ActionCounter', blank=True) # Field name made lowercase.
    logouttime = models.DateTimeField(null=True, db_column='LogoutTime', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'log'

class Lookup(models.Model):
    id = models.IntegerField(primary_key=True)
    klasse = models.CharField(max_length=60)
    code = models.CharField(max_length=60)
    german = models.CharField(max_length=150, db_column='German') # Field name made lowercase.
    dutch = models.CharField(max_length=150, db_column='Dutch') # Field name made lowercase.
    french = models.CharField(max_length=150, db_column='French') # Field name made lowercase.
    italian = models.CharField(max_length=150, db_column='Italian') # Field name made lowercase.
    english = models.CharField(max_length=150, db_column='English') # Field name made lowercase.
    russisch = models.CharField(max_length=150, db_column='Russisch') # Field name made lowercase.
    class Meta:
        db_table = u'lookup'

class Mandant(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    typ = models.CharField(max_length=15, db_column='Typ', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=60, db_column='Name', blank=True) # Field name made lowercase.
    mandantid = models.IntegerField(null=True, db_column='MandantID', blank=True) # Field name made lowercase.
    company = models.CharField(max_length=90, db_column='Company') # Field name made lowercase.
    address1 = models.CharField(max_length=60, db_column='Address1', blank=True) # Field name made lowercase.
    address2 = models.CharField(max_length=60, db_column='Address2', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=60, db_column='Country', blank=True) # Field name made lowercase.
    zip = models.CharField(max_length=30, db_column='ZIP', blank=True) # Field name made lowercase.
    location = models.CharField(max_length=60, db_column='Location', blank=True) # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    baseurl = models.CharField(max_length=450, db_column='BaseURL', blank=True) # Field name made lowercase.
    homesite = models.CharField(max_length=150, db_column='HomeSite', blank=True) # Field name made lowercase.
    lastmodification = models.DateTimeField(null=True, db_column='LastModification', blank=True) # Field name made lowercase.
    lastmodificationby = models.CharField(max_length=60, db_column='LastModificationBy', blank=True) # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    autologouttime = models.IntegerField(db_column='AutoLogoutTime') # Field name made lowercase.
    actualdatalifetime = models.IntegerField(null=True, db_column='ActualDataLifetime', blank=True) # Field name made lowercase.
    defaultlanguage = models.CharField(max_length=60, db_column='DefaultLanguage') # Field name made lowercase.
    timezonename = models.CharField(max_length=192, db_column='TimezoneName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mandant'

class MandantSetting(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    mandantid = models.IntegerField(db_column='MandantID') # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name') # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mandant_setting'

class Mandantimage(models.Model):
    id = models.IntegerField(primary_key=True)
    mandantid = models.IntegerField(unique=True, db_column='MandantID') # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mandantimage'

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=18)
    nr = models.IntegerField()
    bez = models.CharField(max_length=300)
    target = models.CharField(max_length=765, blank=True)
    frame = models.CharField(max_length=60, blank=True)
    rolle = models.CharField(max_length=765, blank=True)
    pos = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'menu'

class Modul(models.Model):
    modulid = models.IntegerField(primary_key=True, db_column='ModulID') # Field name made lowercase.
    mandantid = models.ForeignKey(Mandant, db_column='MandantID') # Field name made lowercase.
    name = models.CharField(max_length=90, db_column='Name') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    state = models.CharField(max_length=36, db_column='State') # Field name made lowercase.
    gprsstate = models.IntegerField(db_column='GprsState') # Field name made lowercase.
    messagecounter = models.IntegerField(db_column='MessageCounter') # Field name made lowercase.
    icon_id = models.IntegerField(null=True, db_column='Icon_ID', blank=True) # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    transportname = models.CharField(max_length=765, db_column='TransportName', blank=True) # Field name made lowercase.
    lastmodification = models.DateTimeField(null=True, db_column='LastModification', blank=True) # Field name made lowercase.
    lastmodificationby = models.CharField(max_length=60, db_column='LastModificationBy', blank=True) # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'modul'

class OverviewCache(models.Model):
    userid = models.IntegerField(primary_key=True, db_column='UserId') # Field name made lowercase.
    fleetid = models.IntegerField(primary_key=True, db_column='FleetId') # Field name made lowercase.
    laststate = models.TextField(db_column='LastState') # Field name made lowercase.
    data = models.TextField(db_column='Data') # Field name made lowercase.
    class Meta:
        db_table = u'overview_cache'

class RelFleetModul(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fleetid = models.ForeignKey(Fleets, db_column='FleetID') # Field name made lowercase.
    modulid = models.ForeignKey(Modul, db_column='ModulID') # Field name made lowercase.
    class Meta:
        db_table = u'rel_fleet_modul'

class RelFleetUser(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fleetid = models.ForeignKey(Fleets, db_column='FleetID') # Field name made lowercase.
    userid = models.ForeignKey('Users', db_column='UserID') # Field name made lowercase.
    class Meta:
        db_table = u'rel_fleet_user'

class ReverseData(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    reversetownid = models.ForeignKey('ReverseTownCache', null=True, db_column='ReverseTownID', blank=True) # Field name made lowercase.
    reversestreetid = models.ForeignKey('ReverseStreetCache', null=True, db_column='ReverseStreetID', blank=True) # Field name made lowercase.
    distance = models.IntegerField(null=True, db_column='Distance', blank=True) # Field name made lowercase.
    direction = models.CharField(max_length=9, db_column='Direction', blank=True) # Field name made lowercase.
    address = models.CharField(max_length=90, db_column='Address', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'reverse_data'

class ReverseDataLast(models.Model):
    id = models.IntegerField(primary_key=True)
    modulid = models.ForeignKey(Modul, db_column='ModulID') # Field name made lowercase.
    reversegeodataid = models.ForeignKey(ReverseData, db_column='ReverseGeoDataID') # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp') # Field name made lowercase.
    class Meta:
        db_table = u'reverse_data_last'

class ReverseStreetCache(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    street = models.CharField(max_length=300, db_column='Street') # Field name made lowercase.
    class Meta:
        db_table = u'reverse_street_cache'

class ReverseTownCache(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    town = models.CharField(max_length=300, db_column='Town') # Field name made lowercase.
    class Meta:
        db_table = u'reverse_town_cache'

class Setting(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(unique=True, max_length=120)
    value = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'setting'

class TblZoneCoords(models.Model):
    id = models.IntegerField(primary_key=True)
    zoneid = models.ForeignKey('TblZoneZone', db_column='ZoneID') # Field name made lowercase.
    posindex = models.IntegerField(db_column='PosIndex') # Field name made lowercase.
    poslat = models.IntegerField(db_column='PosLat') # Field name made lowercase.
    poslon = models.IntegerField(db_column='PosLon') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'tbl_zone_coords'
        verbose_name_plural = u'tbl_zone_coords'

class TblZoneGeogroup(models.Model):
    id = models.IntegerField(primary_key=True)
    mandantid = models.ForeignKey(Mandant, db_column='MandantID') # Field name made lowercase.
    name = models.CharField(unique=True, max_length=135, db_column='Name') # Field name made lowercase.
    syncno = models.IntegerField(db_column='SyncNo') # Field name made lowercase.
    revnr = models.IntegerField(db_column='RevNr') # Field name made lowercase.
    lastmodification = models.DateTimeField(db_column='LastModification') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'tbl_zone_geogroup'

class TblZoneModul(models.Model):
    id = models.IntegerField(primary_key=True)
    modulid = models.ForeignKey(Modul, db_column='ModulID') # Field name made lowercase.
    geogroupid = models.ForeignKey(TblZoneGeogroup, db_column='GeogroupID') # Field name made lowercase.
    class Meta:
        db_table = u'tbl_zone_modul'

class TblZoneType(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=30, db_column='Code') # Field name made lowercase.
    name = models.CharField(max_length=135, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'tbl_zone_type'

class TblZoneZone(models.Model):
    id = models.IntegerField(primary_key=True)
    geogroupid = models.ForeignKey(TblZoneGeogroup, db_column='GeogroupID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    color = models.IntegerField(db_column='Color') # Field name made lowercase.
    zonetypeid = models.ForeignKey(TblZoneType, db_column='ZoneTypeID') # Field name made lowercase.
    radius = models.IntegerField(db_column='Radius') # Field name made lowercase.
    msgindex = models.IntegerField(db_column='MsgIndex') # Field name made lowercase.
    msgsubindex = models.IntegerField(db_column='MsgSubIndex') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    groupset = models.IntegerField(db_column='GroupSet') # Field name made lowercase.
    class Meta:
        db_table = u'tbl_zone_zone'

class Text(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=150, db_column='Type', blank=True) # Field name made lowercase.
    page = models.CharField(max_length=150, db_column='Page', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name', blank=True) # Field name made lowercase.
    german = models.TextField(db_column='German', blank=True) # Field name made lowercase.
    dutch = models.TextField(db_column='Dutch', blank=True) # Field name made lowercase.
    french = models.TextField(db_column='French', blank=True) # Field name made lowercase.
    italian = models.TextField(db_column='Italian', blank=True) # Field name made lowercase.
    english = models.TextField(db_column='English', blank=True) # Field name made lowercase.
    russisch = models.TextField(db_column='Russisch', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'text'

class TimetableCancellation(models.Model):
    id = models.IntegerField(primary_key=True)
    timetabletransportid = models.ForeignKey('TimetableTransport', db_column='TimetableTransportId') # Field name made lowercase.
    cancellation = models.IntegerField(db_column='Cancellation') # Field name made lowercase.
    from_field = models.DateField(db_column='From') # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.DateField(db_column='To') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_cancellation'

class TimetableComment(models.Model):
    id = models.IntegerField(primary_key=True)
    timetablerunningsequenceid = models.IntegerField(db_column='TimetableRunningSequenceId') # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=30, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_comment'

class TimetableComposition(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90, db_column='Name') # Field name made lowercase.
    linie = models.CharField(max_length=90, db_column='Linie') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_composition'

class TimetablePeriode(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=300, db_column='Description') # Field name made lowercase.
    from_field = models.DateField(db_column='From') # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.DateField(db_column='To') # Field name made lowercase.
    mandantid = models.IntegerField(db_column='MandantID') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_periode'

class TimetablePeriodeDay(models.Model):
    id = models.IntegerField(primary_key=True)
    timetableperiodeid = models.ForeignKey(TimetablePeriode, db_column='TimetablePeriodeId') # Field name made lowercase.
    timetabletransportid = models.ForeignKey('TimetableTransport', db_column='TimetableTransportId') # Field name made lowercase.
    day = models.CharField(unique=True, max_length=81, db_column='Day') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_periode_day'

class TimetablePeriodeDayException(models.Model):
    id = models.IntegerField(primary_key=True)
    timetableperiodeid = models.ForeignKey(TimetablePeriode, db_column='TimetablePeriodeId') # Field name made lowercase.
    description = models.CharField(max_length=150, db_column='Description') # Field name made lowercase.
    date = models.DateField(unique=True, db_column='Date') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_periode_day_exception'

class TimetablePeriodeDayExceptionTransport(models.Model):
    id = models.IntegerField(primary_key=True)
    timetableperiodedayexceptionid = models.ForeignKey(TimetablePeriodeDayException, db_column='TimetablePeriodeDayExceptionId') # Field name made lowercase.
    timetabletransportid = models.IntegerField(db_column='TimetableTransportId') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_periode_day_exception_transport'

class TimetableRelation(models.Model):
    id = models.IntegerField(primary_key=True)
    timetableperiodeid = models.ForeignKey(TimetablePeriode, db_column='TimetablePeriodeId') # Field name made lowercase.
    monitoring = models.CharField(max_length=24, db_column='Monitoring', blank=True) # Field name made lowercase.
    geogroupid = models.ForeignKey(TblZoneGeogroup, db_column='GeogroupId') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    mandantid = models.IntegerField(db_column='MandantID') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_relation'

class TimetableRelationCheckpoint(models.Model):
    id = models.IntegerField(primary_key=True)
    timetablerelationid = models.ForeignKey(TimetableRelation, db_column='TimetableRelationId') # Field name made lowercase.
    checkpointtype = models.CharField(max_length=12, db_column='CheckpointType') # Field name made lowercase.
    position = models.IntegerField(db_column='Position') # Field name made lowercase.
    zoneid = models.ForeignKey(TblZoneZone, null=True, db_column='ZoneID', blank=True) # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_relation_checkpoint'

class TimetableReportRunningSequence(models.Model):
    id = models.IntegerField(primary_key=True)
    timetablerunningstatusid = models.ForeignKey('TimetableReportRunningStatus', db_column='TimetableRunningStatusId') # Field name made lowercase.
    checkpointtype = models.CharField(max_length=12, db_column='CheckpointType', blank=True) # Field name made lowercase.
    zoneid = models.IntegerField(null=True, db_column='ZoneID', blank=True) # Field name made lowercase.
    position = models.IntegerField(db_column='Position') # Field name made lowercase.
    scheduledarrival = models.DateTimeField(null=True, db_column='ScheduledArrival', blank=True) # Field name made lowercase.
    realarrival = models.DateTimeField(null=True, db_column='RealArrival', blank=True) # Field name made lowercase.
    scheduleddeparture = models.DateTimeField(null=True, db_column='ScheduledDeparture', blank=True) # Field name made lowercase.
    realdeparture = models.DateTimeField(null=True, db_column='RealDeparture', blank=True) # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_report_running_sequence'

class TimetableReportRunningStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    date = models.DateField(db_column='Date') # Field name made lowercase.
    peerid = models.IntegerField(null=True, db_column='PeerID', blank=True) # Field name made lowercase.
    timetableperiodeid = models.ForeignKey(TimetablePeriode, db_column='TimetablePeriodeId') # Field name made lowercase.
    timetabletransportid = models.ForeignKey('TimetableTransport', db_column='TimetableTransportId') # Field name made lowercase.
    position = models.IntegerField(db_column='Position') # Field name made lowercase.
    direction = models.CharField(max_length=9, db_column='Direction', blank=True) # Field name made lowercase.
    status = models.CharField(max_length=39, db_column='Status') # Field name made lowercase.
    otmileage = models.IntegerField(db_column='OTMileage') # Field name made lowercase.
    curmileage = models.IntegerField(db_column='CurMileage') # Field name made lowercase.
    composition = models.IntegerField(null=True, db_column='Composition', blank=True) # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_report_running_status'

class TimetableRunningSequence(models.Model):
    id = models.IntegerField(primary_key=True)
    timetablerunningstatusid = models.ForeignKey('TimetableRunningStatus', db_column='TimetableRunningStatusId') # Field name made lowercase.
    checkpointtype = models.CharField(max_length=12, db_column='CheckpointType', blank=True) # Field name made lowercase.
    zoneid = models.IntegerField(null=True, db_column='ZoneID', blank=True) # Field name made lowercase.
    position = models.IntegerField(db_column='Position') # Field name made lowercase.
    scheduledarrival = models.DateTimeField(null=True, db_column='ScheduledArrival', blank=True) # Field name made lowercase.
    realarrival = models.DateTimeField(null=True, db_column='RealArrival', blank=True) # Field name made lowercase.
    scheduleddeparture = models.DateTimeField(null=True, db_column='ScheduledDeparture', blank=True) # Field name made lowercase.
    realdeparture = models.DateTimeField(null=True, db_column='RealDeparture', blank=True) # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_running_sequence'

class TimetableRunningStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    date = models.DateField(db_column='Date') # Field name made lowercase.
    peerid = models.IntegerField(null=True, db_column='PeerID', blank=True) # Field name made lowercase.
    timetableperiodeid = models.IntegerField(db_column='TimetablePeriodeId') # Field name made lowercase.
    timetabletransportid = models.IntegerField(db_column='TimetableTransportId') # Field name made lowercase.
    position = models.IntegerField(db_column='Position') # Field name made lowercase.
    direction = models.CharField(max_length=9, db_column='Direction', blank=True) # Field name made lowercase.
    status = models.CharField(max_length=39, db_column='Status') # Field name made lowercase.
    otmileage = models.IntegerField(db_column='OTMileage') # Field name made lowercase.
    curmileage = models.IntegerField(db_column='CurMileage') # Field name made lowercase.
    composition = models.IntegerField(null=True, db_column='Composition', blank=True) # Field name made lowercase.
    extpeerid = models.IntegerField(null=True, db_column='ExtPeerID', blank=True) # Field name made lowercase.
    extcomposition = models.IntegerField(null=True, db_column='ExtComposition', blank=True) # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_running_status'

class TimetableTransport(models.Model):
    id = models.IntegerField(primary_key=True)
    timetableperiodeid = models.ForeignKey(TimetablePeriode, db_column='TimetablePeriodeId') # Field name made lowercase.
    timetablerelationid = models.ForeignKey(TimetableRelation, db_column='TimetableRelationId') # Field name made lowercase.
    monitoring = models.CharField(max_length=24, db_column='Monitoring') # Field name made lowercase.
    direction = models.CharField(max_length=9, db_column='Direction') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    version = models.IntegerField(db_column='Version') # Field name made lowercase.
    mandantid = models.IntegerField(db_column='MandantID') # Field name made lowercase.
    timezonename = models.CharField(max_length=192, db_column='TimezoneName') # Field name made lowercase.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_transport'

class TimetableTransporttime(models.Model):
    id = models.IntegerField(primary_key=True)
    timetabletransportid = models.ForeignKey(TimetableTransport, db_column='TimetableTransportId') # Field name made lowercase.
    timetablerelationcheckpointid = models.ForeignKey(TimetableRelationCheckpoint, db_column='TimetableRelationCheckpointId') # Field name made lowercase.
    arrival = models.TextField(db_column='Arrival', blank=True) # Field name made lowercase. This field type is a guess.
    departure = models.TextField(db_column='Departure', blank=True) # Field name made lowercase. This field type is a guess.
    lastmodifiedby = models.CharField(max_length=90, db_column='LastModifiedBy') # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified') # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    class Meta:
        db_table = u'timetable_transporttime'

class Users(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    mandantid = models.ForeignKey(Mandant, null=True, db_column='MandantID', blank=True) # Field name made lowercase.
    username = models.CharField(unique=True, max_length=60, db_column='UserName') # Field name made lowercase.
    password = models.CharField(max_length=180, db_column='Password') # Field name made lowercase.
    accesslevel = models.ForeignKey(AccessLevel, db_column='AccessLevel') # Field name made lowercase.
    amountoftablerows = models.IntegerField(null=True, db_column='AmountOfTableRows', blank=True) # Field name made lowercase.
    maxnumberofresults = models.IntegerField(null=True, db_column='MaxNumberOfResults', blank=True) # Field name made lowercase.
    language = models.CharField(max_length=60, db_column='Language') # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    refresh_time = models.IntegerField(null=True, db_column='Refresh_Time', blank=True) # Field name made lowercase.
    lastmodification = models.DateTimeField(null=True, db_column='LastModification', blank=True) # Field name made lowercase.
    lastmodificationby = models.CharField(max_length=60, db_column='LastModificationBy', blank=True) # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateOfCreation') # Field name made lowercase.
    loggontime = models.DateTimeField(null=True, db_column='LoggOnTime', blank=True) # Field name made lowercase.
    loggontimeinmillis = models.CharField(max_length=90, db_column='LoggOnTimeInMillis', blank=True) # Field name made lowercase.
    wrongloginattempts = models.IntegerField(null=True, db_column='WrongLoginAttempts', blank=True) # Field name made lowercase.
    timeofwronglogin = models.CharField(max_length=90, db_column='TimeOfWrongLogin', blank=True) # Field name made lowercase.
    vorname = models.CharField(max_length=150, db_column='Vorname', blank=True) # Field name made lowercase.
    nachname = models.CharField(max_length=150, db_column='Nachname', blank=True) # Field name made lowercase.
    anschrift = models.TextField(db_column='Anschrift', blank=True) # Field name made lowercase.
    telefon = models.CharField(max_length=150, db_column='Telefon', blank=True) # Field name made lowercase.
    telefax = models.CharField(max_length=150, db_column='Telefax', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=150, db_column='Email', blank=True) # Field name made lowercase.
    timezonename = models.CharField(max_length=192, db_column='TimezoneName', blank=True) # Field name made lowercase.
    googleloadcounter = models.IntegerField(db_column='GoogleLoadCounter') # Field name made lowercase.
    class Meta:
        db_table = u'users'
        verbose_name_plural = u'Users'

class UsersSetting(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name') # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'users_setting'

class ZoneLinegraph(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    modulid = models.BigIntegerField(db_column='ModulID') # Field name made lowercase.
    zoneid = models.BigIntegerField(db_column='ZoneID') # Field name made lowercase.
    mileage = models.BigIntegerField(db_column='Mileage') # Field name made lowercase.
    evtime = models.DateTimeField(db_column='EvTime') # Field name made lowercase.
    direction = models.CharField(max_length=6, db_column='Direction', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'zone_linegraph'

