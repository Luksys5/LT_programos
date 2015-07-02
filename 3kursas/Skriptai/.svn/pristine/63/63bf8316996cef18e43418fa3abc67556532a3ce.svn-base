#
# ovid2tex: converts literature database format
#           from OVID to BiBTeX format
#           with labels as described in 'bibsearch'
#           manpage
#           5.2.1996 AB
#               
{
  # switch to several analyse modes for storing STDIN (AUTHOR,TITLE,JOURNAL) 
  # or make Layout (END)
  #
  ############## AMODE definition ################
  #
  if ( $0 ~ /^[A-Z]/ )     AMODE=" "
  #
  if ( $0 ~ /^Registry/ )  AMODE="END"
  #
  if ( $0 ~ /^Author/ )  { AMODE="AUTHOR"; iauth=0 }
  #
  if ( $0 ~ /^Title/ )   { AMODE="TITLE";  ititl=0 }  
  #
  if ( $0 ~ /^Source/ )  { AMODE="SOURCE"; ijour=0 }
  #
  ################## AMODE actions ################
  #
  if ( AMODE == "AUTHOR" && $0 != "Authors" )
     {
       for ( i = 1;  i <= NF ; i++ )
           {
              iauth=iauth+1
              NAME[iauth]=$i
           }
     }
  #
  if ( AMODE == "TITLE" && $0 != "Title" )
     {
         ititl=ititl+1
         TITLINE[ititl]=$0
     }
  #
  if ( AMODE == "SOURCE" && $0 != "Source" )
     {
          ijour=ijour+1
          JOURLINE[ijour]=$0
     }
  #
  ############## AMODE = END --> layout #############
  #
  if ( AMODE == "END" )
     {
      # LABEL from max. 5 authors
      LABEL=""
      for ( i = 1 ; i <= iauth ; i=i+2 )
          {
             if ( i < 11 )
             {
                LETTER=substr(NAME[i],1,1)
                LABEL=LABEL LETTER
             }
          }
      #
      JDATA=""
      for ( i = 1 ; i <= ijour ; i++ )
          {
             JDATA=JDATA JOURLINE[i]
          }
      split(JDATA,JDF1,".")
      JOURNAL_VOL=JDF1[1]
      YEAR=JDF1[2]
      PAGES=JDF1[3]
      split(PAGES,JDF2,"-")
      LPAGETMP=JDF2[1]
      split(LPAGETMP,LPAGE," ")   #remove ' ' from string
      LYEAR=substr(YEAR,4,2)
      LABEL=LABEL "_" LYEAR "_" LPAGE[1]
      #
      NUMM=split(JOURNAL_VOL,JDF3," ")
      JOURNAL=" "
      VOL=" "
      
      for ( ii = 1 ; ii <= NUMM ; ii++ )
         {
             if ( JDF3[ii] ~ /[0-9]/ )
                {
                  VOL=VOL" "JDF3[ii]
                }
                else
                {
                   JOURNAL =JOURNAL" "JDF3[ii]
                }
         }
      printf "@article{%-15s,\n",LABEL
      printf "     author = {" 
      for ( i = 1 ; i <= iauth ; i=i+2 )
          {
          if ( i == 1 )
             {
               SPACE=" "
             }
          else
             {
               SPACE="                 "
             }
          #
              if ( i != iauth-1 )
               {
                  print SPACE,NAME[i+1],NAME[i]," and "
               }
             else
               {
                  print SPACE,NAME[i+1],NAME[i]," },"
                  #printf "\n"
               }
          }
          ###
      SPACE="    "
      print  SPACE,"journal = {",JOURNAL," },"
      print  SPACE,"year    = {",YEAR," },"
      print  SPACE,"volume  = {",VOL," },"
      print  SPACE,"pages   = {",PAGES," },"
      printf "     title   = {" 
      for ( i = 1 ; i <= ititl ; i++ )
          {
          if ( i == 1 )
             {
               SPACE=" "
             }
          else
             {
               SPACE="              "
             }
          #
             if ( i > ititl-1 )
               {
                  print SPACE,TITLINE[i]," }}"
                  printf "\n"
               }
             else
               {
                  print SPACE,TITLINE[i]
               }
          }
      #
      AMODE = " "
    }
}










