# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Advertisement(models.Model):
    ad_code = models.AutoField(primary_key=True)  # The composite primary key (ad_code, estate_agency_aid, estate_agency_region_region_id, estate_agency_region_city_city_id, estate_agency_region_estate_agency_aid, agency_manager_manager_id, agency_manager_user_user_id, agency_manager_estate_agency_aid, agency_manager_estate_agency_region_region_id, agency_manager_estate_agency_region_city_city_id, agency_manager_estate_agency_region_estate_agency_aid) found, that is not supported. The first column is selected.
    ad_title = models.CharField(max_length=255)
    mortgage = models.IntegerField()
    rent = models.IntegerField()
    buy = models.IntegerField()
    main_image = models.TextField()
    image_1 = models.TextField(blank=True, null=True)
    image_2 = models.TextField(blank=True, null=True)
    image_3 = models.TextField(blank=True, null=True)
    image_4 = models.TextField(blank=True, null=True)
    image_5 = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=511, blank=True, null=True)
    exchange = models.IntegerField()
    collaborative = models.IntegerField()
    convertable = models.IntegerField()
    presell = models.IntegerField()
    administrative_position = models.IntegerField()
    borrower = models.IntegerField()
    newly_built = models.IntegerField()
    in_proportionate_share = models.IntegerField()
    estate_agency_aid = models.IntegerField(unique=True)
    estate_agency_region_region_id = models.IntegerField(unique=True)
    estate_agency_region_city_city_id = models.IntegerField(unique=True)
    estate_agency_region_estate_agency_aid = models.IntegerField(unique=True)
    agency_manager_manager = models.OneToOneField('AgencyManager', models.DO_NOTHING)
    agency_manager_user_user = models.OneToOneField('AgencyManager', models.DO_NOTHING, related_name='advertisement_agency_manager_user_user_set')
    agency_manager_estate_agency_aid = models.OneToOneField('AgencyManager', models.DO_NOTHING, db_column='agency_manager_estate_agency_aid', related_name='advertisement_agency_manager_estate_agency_aid_set')
    agency_manager_estate_agency_region_region = models.OneToOneField('AgencyManager', models.DO_NOTHING, related_name='advertisement_agency_manager_estate_agency_region_region_set')
    agency_manager_estate_agency_region_city_city = models.OneToOneField('AgencyManager', models.DO_NOTHING, related_name='advertisement_agency_manager_estate_agency_region_city_city_set')
    agency_manager_estate_agency_region_estate_agency_aid = models.OneToOneField('AgencyManager', models.DO_NOTHING, db_column='agency_manager_estate_agency_region_estate_agency_aid', related_name='advertisement_agency_manager_estate_agency_region_estate_agency_aid_set')

    class Meta:
        managed = False
        db_table = 'advertisement'
        unique_together = (('ad_code', 'estate_agency_aid', 'estate_agency_region_region_id', 'estate_agency_region_city_city_id', 'estate_agency_region_estate_agency_aid', 'agency_manager_manager', 'agency_manager_user_user', 'agency_manager_estate_agency_aid', 'agency_manager_estate_agency_region_region', 'agency_manager_estate_agency_region_city_city', 'agency_manager_estate_agency_region_estate_agency_aid'),)


class AgencyManager(models.Model):
    manager_id = models.AutoField(primary_key=True)  # The composite primary key (manager_id, user_user_id, estate_agency_aid, estate_agency_region_region_id, estate_agency_region_city_city_id, estate_agency_region_estate_agency_aid) found, that is not supported. The first column is selected.
    user_user = models.OneToOneField('User', models.DO_NOTHING)
    estate_agency_aid = models.OneToOneField('EstateAgency', models.DO_NOTHING, db_column='estate_agency_aid')
    estate_agency_region_region = models.OneToOneField('EstateAgency', models.DO_NOTHING, related_name='agencymanager_estate_agency_region_region_set')
    estate_agency_region_city_city = models.OneToOneField('EstateAgency', models.DO_NOTHING, related_name='agencymanager_estate_agency_region_city_city_set')
    estate_agency_region_estate_agency_aid = models.OneToOneField('EstateAgency', models.DO_NOTHING, db_column='estate_agency_region_estate_agency_aid', related_name='agencymanager_estate_agency_region_estate_agency_aid_set')

    class Meta:
        managed = False
        db_table = 'agency_manager'
        unique_together = (('manager_id', 'user_user', 'estate_agency_aid', 'estate_agency_region_region', 'estate_agency_region_city_city', 'estate_agency_region_estate_agency_aid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    city_id = models.AutoField(primary_key=True)  # The composite primary key (city_id, province_pid) found, that is not supported. The first column is selected.
    city_name = models.CharField(max_length=255)
    province_pid = models.OneToOneField('Province', models.DO_NOTHING, db_column='province_pid')

    class Meta:
        managed = False
        db_table = 'city'
        unique_together = (('city_id', 'province_pid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstateAgency(models.Model):
    aid = models.AutoField(primary_key=True)  # The composite primary key (aid, region_region_id, region_city_city_id, region_estate_agency_aid) found, that is not supported. The first column is selected.
    aname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    aphone = models.IntegerField()
    no_of_employees = models.IntegerField()
    alogo = models.TextField()
    region_region = models.OneToOneField('Region', models.DO_NOTHING)
    region_city_city = models.OneToOneField('Region', models.DO_NOTHING, related_name='estateagency_region_city_city_set')
    region_estate_agency_aid = models.OneToOneField('Region', models.DO_NOTHING, db_column='region_estate_agency_aid', related_name='estateagency_region_estate_agency_aid_set')

    class Meta:
        managed = False
        db_table = 'estate_agency'
        unique_together = (('aid', 'region_region', 'region_city_city', 'region_estate_agency_aid'),)


class House(models.Model):
    address = models.CharField(max_length=255)
    area = models.IntegerField()
    year = models.IntegerField()
    house_id = models.AutoField(primary_key=True)  # The composite primary key (house_id, region_region_id, region_city_city_id, advertisement_ad_code, advertisement_estate_agency_aid, advertisement_estate_agency_region_region_id, advertisement_estate_agency_region_city_city_id, advertisement_estate_agency_region_estate_agency_aid) found, that is not supported. The first column is selected.
    rooms = models.IntegerField()
    creation_time = models.DateTimeField()
    elevator = models.IntegerField()
    balcony = models.IntegerField()
    parking = models.IntegerField()
    storage_area = models.IntegerField()
    security_guard = models.IntegerField()
    loby_area = models.IntegerField()
    pool = models.IntegerField()
    sauna = models.IntegerField()
    jacuzzi = models.IntegerField()
    sports_hall_area = models.IntegerField()
    air_conditioning = models.IntegerField()
    conference_hall = models.IntegerField()
    central_antenna = models.IntegerField()
    remote_door = models.IntegerField()
    roof_garden = models.IntegerField()
    type = models.CharField(max_length=150)
    region_region = models.OneToOneField('Region', models.DO_NOTHING)
    region_city_city = models.OneToOneField('Region', models.DO_NOTHING, related_name='house_region_city_city_set')
    advertisement_ad_code = models.OneToOneField(Advertisement, models.DO_NOTHING, db_column='advertisement_ad_code')
    advertisement_estate_agency_aid = models.OneToOneField(Advertisement, models.DO_NOTHING, db_column='advertisement_estate_agency_aid', related_name='house_advertisement_estate_agency_aid_set')
    advertisement_estate_agency_region_region = models.OneToOneField(Advertisement, models.DO_NOTHING, related_name='house_advertisement_estate_agency_region_region_set')
    advertisement_estate_agency_region_city_city = models.OneToOneField(Advertisement, models.DO_NOTHING, related_name='house_advertisement_estate_agency_region_city_city_set')
    advertisement_estate_agency_region_estate_agency_aid = models.OneToOneField(Advertisement, models.DO_NOTHING, db_column='advertisement_estate_agency_region_estate_agency_aid', related_name='house_advertisement_estate_agency_region_estate_agency_aid_set')

    class Meta:
        managed = False
        db_table = 'house'
        unique_together = (('house_id', 'region_region', 'region_city_city', 'advertisement_ad_code', 'advertisement_estate_agency_aid', 'advertisement_estate_agency_region_region', 'advertisement_estate_agency_region_city_city', 'advertisement_estate_agency_region_estate_agency_aid'),)


class HouseHasEstateAgency(models.Model):
    house_house = models.OneToOneField(House, models.DO_NOTHING, primary_key=True)  # The composite primary key (house_house_id, house_region_region_id, house_region_city_city_id, estate_agency_aid, estate_agency_region_region_id, estate_agency_region_city_city_id, estate_agency_region_estate_agency_aid) found, that is not supported. The first column is selected.
    house_region_region = models.OneToOneField(House, models.DO_NOTHING, related_name='househasestateagency_house_region_region_set')
    house_region_city_city = models.OneToOneField(House, models.DO_NOTHING, related_name='househasestateagency_house_region_city_city_set')
    estate_agency_aid = models.OneToOneField(EstateAgency, models.DO_NOTHING, db_column='estate_agency_aid')
    estate_agency_region_region = models.OneToOneField(EstateAgency, models.DO_NOTHING, related_name='househasestateagency_estate_agency_region_region_set')
    estate_agency_region_city_city = models.OneToOneField(EstateAgency, models.DO_NOTHING, related_name='househasestateagency_estate_agency_region_city_city_set')
    estate_agency_region_estate_agency_aid = models.OneToOneField(EstateAgency, models.DO_NOTHING, db_column='estate_agency_region_estate_agency_aid', related_name='househasestateagency_estate_agency_region_estate_agency_aid_set')

    class Meta:
        managed = False
        db_table = 'house_has_estate_agency'
        unique_together = (('house_house', 'house_region_region', 'house_region_city_city', 'estate_agency_aid', 'estate_agency_region_region', 'estate_agency_region_city_city', 'estate_agency_region_estate_agency_aid'),)


class Province(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'province'


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)  # The composite primary key (region_id, city_city_id, estate_agency_aid) found, that is not supported. The first column is selected.
    region_name = models.CharField(max_length=255)
    city_city = models.OneToOneField(City, models.DO_NOTHING)
    estate_agency_aid = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'region'
        unique_together = (('region_id', 'city_city', 'estate_agency_aid'),)


class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    creation_time = models.DateTimeField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user'
