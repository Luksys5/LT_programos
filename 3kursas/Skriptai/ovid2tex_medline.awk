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
  if ( $0 ~ /^[A-Z]/ )      AMODE=" "
  #
  if  ( $0 ~ /^MeSH|^Abstract|^Registry/ )
     AMODE="END"
  #
  if ( $0 ~ /^Author/ )  { AMODE="AUTHOR"; iauth=0; done=0 }
  #
  if ( $0 ~ /^Title/ )   { AMODE="TITLE";  ititl=0; done=0 }  
  #
  if ( $0 ~ /^Source/ )  { AMODE="SOURCE"; ijour=0; done=0 }
  #
  ################## AMODE actions ################
  #
  if ( AMODE == "AUTHOR" && $0 != "Authors" )
     {
       curr_iauth = split ($0, CURRENT_NAMES, ".") - 1
       for( i = 1; i <= curr_iauth; i++ )
            NAME[iauth + i] = CURRENT_NAMES[i]
       iauth += curr_iauth;
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
  if ( AMODE == "END" && !done )
     {
      # LABEL from max. 5 authors
      LABEL=""
      for ( i = 1 ; i <= min(iauth, 5) ; i++ )
          {
            split(NAME[i], INITIALS)
            LETTER=substr(INITIALS[1],1,1)
            LABEL=LABEL LETTER
          }
      #
      JDATA=""
      for ( i = 1 ; i <= ijour ; i++ )
          {
             JDATA=JDATA JOURLINE[i]
          }
      split(JDATA,JDF1,".")
      JOURNAL=JDF1[1]
      split(JDF1[2],JDF2,":")
      VOL=JDF2[1]
      split(JDF2[2],JDF3,",")
      PAGES=JDF3[1]
      split(JDF3[2],JDF4," ")
      YEAR=JDF4[1]
      LYEAR=substr(YEAR,3,2)
      split(PAGES,JDF5,"-")
      LPAGE=JDF5[1]
      LABEL=LABEL "_" LYEAR "_" LPAGE
      #
      printf "@article{%-15s,\n",LABEL
      printf "     author = {" 
      for ( i = 1 ; i <= iauth ; i++ )
          {
          printf "%s", ( i == 1 ) ? " " : "                 "

          iInitials = split(NAME[i], INITIALS)
          printf "%s.", INITIALS[iInitials]
          for( j = 1; j < iInitials; j++ ) 
               {
          	  printf " %s", INITIALS[j]
               }
          print (i < iauth) ? " and " : " },"
          }
          
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
      done = 1
    }
}

function min(x,y)
{
  return (x < y) ? x : y
}
