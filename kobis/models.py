from django.contrib.postgres.fields import JSONField
from django.db import models


class People(models.Model):
    peopleCd = models.CharField(max_length=10, unique=True)
    peopleNm = models.CharField(max_length=10)
    peopleNmEn = models.CharField(max_length=30)
    repRoleNm = models.CharField(max_length=10)
    filmoNames = models.TextField()


class Companies(models.Model):
    companyCd = models.CharField(max_length=10, unique=True)
    companyNm = models.CharField(max_length=50)
    companyNmEn = models.CharField(max_length=50)
    companyPartNames = models.CharField(max_length=30)
    ceoNm = models.CharField(max_length=20)
    filmoNames = models.TextField()


class Movies(models.Model):
    movieCd = models.CharField(max_length=10, unique=True)
    movieNm = models.TextField()
    movieNmEn = models.TextField()
    prdtYear = models.CharField(max_length=10)
    openDt = models.CharField(max_length=10)
    typeNm = models.CharField(max_length=10)
    prdtStatNm = models.CharField(max_length=10)
    nationAlt = models.CharField(max_length=30)
    genreAlt = models.CharField(max_length=30)
    repNationNm = models.CharField(max_length=10)
    repGenreNm = models.CharField(max_length=10)
    directors = models.ManyToManyField(People, related_name='Movies_director')
    companys = models.ManyToManyField(Companies, related_name='Movies_company')


class Boxoffice(models.Model):
    boxofficeType = models.CharField(max_length=20)
    showRange = models.CharField(max_length=20, unique=True)
    yearWeekTime = models.CharField(max_length=10)
    rnum = models.CharField(max_length=10)
    rank = models.CharField(max_length=10)
    rankInten = models.CharField(max_length=10)
    rankOldAndNew = models.CharField(max_length=10)
    movieCd = models.ForeignKey(Movies, related_name='Boxoffice_movieCd')
    movieNm = models.ForeignKey(Movies, related_name='Boxoffice_movieNm')
    openDt = models.ForeignKey(Movies, related_name='Boxoffice_openDt')
    salesAmt = models.CharField(max_length=20)
    salesShare = models.CharField(max_length=10)
    salesInten = models.CharField(max_length=20)
    salesChange = models.CharField(max_length=10)
    salesAcc = models.CharField(max_length=20)
    audiCnt = models.CharField(max_length=10)
    audiInten = models.CharField(max_length=10)
    audiChange = models.CharField(max_length=10)
    audiAcc = models.CharField(max_length=20)
    scrnCnt = models.CharField(max_length=10)
    showCnt = models.CharField(max_length=10)


class MovieDetails(models.Model):
    movieCd = models.ForeignKey(Movies, related_name='MovieDetails_movieCd')
    movieNm = models.ForeignKey(Movies, related_name='MovieDetails_movieNm')
    movieNmEn = models.ForeignKey(Movies, related_name='MovieDetails_movieNmEn')
    movieNmOg = models.TextField()
    prdtYear = models.ForeignKey(Movies, related_name='MovieDetails_prdtYear')
    showTm = models.CharField(max_length=10)
    openDt = models.ForeignKey(Movies, related_name='MovieDetails_openDt')
    prdtStatNm = models.ForeignKey(Movies, related_name='MovieDetails_prdtStatNm')
    typeNm = models.ForeignKey(Movies, related_name='MovieDetails_typeNm')
    nations = models.TextField()
    genre = models.TextField()
    directors = models.TextField()
    actors = models.TextField()
    showTypes = models.TextField()
    audits = models.TextField()
    companys = models.TextField()
    staffs = models.TextField()


class CompanyDetails(models.Model):
    companyCd = models.ForeignKey(Companies, related_name='CompanyDetails_companyCd')
    companyNm = models.ForeignKey(Companies, related_name='CompanyDetails_companyNm')
    companyNmEn = models.ForeignKey(Companies, related_name='CompanyDetails_companyNmEn')
    ceoNm = models.ForeignKey(Companies, related_name='CompanyDetails_ceoNm')
    parts = models.TextField()
    filmos = models.TextField()


class PersonDetails(models.Model):
    peopleCd = models.ForeignKey(People, related_name='PersonDetails_peopleCd')
    peopleNm = models.ForeignKey(People, related_name='PersonDetails_peopleNm')
    peopleNmEn = models.ForeignKey(People, related_name='PersonDetails_peopleNmEn')
    sex = models.CharField(max_length=10)
    repRoleNm = models.ForeignKey(People, related_name='PersonDetails_repRoleNm')
    filmos = models.TextField()
    homepages = models.CharField(max_length=50)
