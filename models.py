# -*- coding: latin-1 -*-
from django.db import models
from datetime  import  datetime
from connection import get_connection
from django.contrib.auth.models import User
from datetime import date, timedelta
class ConseillerCommercial(User):
    log  = models.CharField(max_length = 200)

    def __repr__(self):
      return  "CC |%s" % self.name

    def isstaff(self):
      return self.is_staff

    def tostaff(self):
      self.is_staff = True

    @classmethod
    def rbon_check(cls, user):
      con =  get_connection()
      print 'con' , con
      cur = con.cursor()
      print 'cur' , cur

      yesterday  =  date.today()-timedelta(days=1)
      last_week  = [ (yesterday - timedelta(days =d)).strftime('%d/%m/%Y')
                     for d in range(7)]
      last_month = [ (yesterday - timedelta(days=d)).strftime('%d/%m/%Y')
                     for d in range(30)]
      yesterday  = [  yesterday.strftime('%d/%m/%Y') ]
      print 'yesterday' , yesterday
      print 'last_month' , last_month
      print 'last_week' , last_week
    
      query ="""
            select  
            sum(cast(VCPLUS as integer)), sum(cast(VCMOIN as integer)),
            sum(cast(UPPLUS as integer)), sum(cast(UPMOIN as integer)),
            sum(cast(TOTAL as integer)), sum(cast(CA_Emission as integer)),
            sum(cast(RA_Appels_traites as integer))
            FROM Main_Rebons 
            where JOURNEE in (?)
            And upper(usercre) in ('#')
            group by usercre
      """
      out = {'user_yesterday':[], 'user_week':[],'user_month':[]}
      
      for list , flag in  [(last_week , 'user_week'), (last_month , 'user_month'), (yesterday, 'user_yesterday')]:
            query2  = query.replace('?', ",".join(
                            map( lambda e: "'%s'"%e , list)))
            #query2  = query2.replace('#' , user.username)
            query2  = query2.replace('#' , 'PCCI87')
            print query2
            cur.execute(query2)
            out[flag]  = cur.fetchall()
            
      # The best
      
      
      query ="""
            select  
            sum(cast(VCPLUS as integer)), sum(cast(VCMOIN as integer)),
            sum(cast(UPPLUS as integer)), sum(cast(UPMOIN as integer)),
            sum(cast(TOTAL as integer)), sum(cast(CA_Emission as integer)),
            sum(cast(RA_Appels_traites as integer))
            FROM Main_Rebons 
            where JOURNEE in (?)
            group by usercre
            order by  sum(cast(TOTAL as integer)) desc
      """
      out2 = {'max_yesterday':[], 'max_week':[],'max_month':[]}
      
      for list , flag in  [(last_week , 'max_week'), (last_month , 'max_month'), (yesterday, 'max_yesterday')]:
            query2  = query.replace('?', ",".join(
                            map( lambda e: "'%s'"%e,list )))
            query2  = query2.replace('#' , user.username)
            print query2
            cur.execute(query2)
            out2[flag]  = [cur.fetchall()[0]]
      return out, out2     
        

class RebonWrapper(object):
    def __init__(self):
        journee  = None
        usercre  = None
        vcplus   = None
        vcmoin   = None
        uplus    = None
        umoins   = None
        total    = None
        pcci_user= None
        ca_emission =None
        ra_appelstraites =None
        
    @classmethod
    def fill(data):
        rebons = []
        for d in data:
            rebons.appen(RebonWrapper(d))
        return rebons
    
    def __repr__(self):
        return "RebonWrapper | %s | %s" %(
             self.journee, self.total)
      


