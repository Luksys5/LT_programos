#!/bin/sh
#!perl  -w
eval 'exec perl -x $0 ${1+"$@"}'
    if 0;
#-----------------------------------------------------------------------
#  mapperl -- print the parameters from the CCP4 map header
#-----------------------------------------------------------------------
#$Author: grazulis $
#$Date: 1998/01/23 12:45:11 $
#$Header:
#$Locker:  $
#$Revision: 1.4 $
#$Source: /kaefer/u05/grazulis/src/CCE/scripts/RCS/mapdump,v $
#$State: Exp $
#-----------------------------------------------------------------------
# Dump header information of a CCP4 binary map
#
#INPUT:
#   one or several CCP4 map files on the command line
#
#OUTPUT:
#   parameters from map header of each file
#
#-----------------------------------------------------------------------

use strict;
use GetOptions;
use CCP4Map;

$, = " "; $\ = "\n"; $" = ", ";

die("Need map file on the command line") unless @ARGV > 0;

foreach (@ARGV) {
    my %map_header = ();
    print "\nFile: $_";
    eval{ CCP4Map::readMapHeader($_, \%map_header) };
    print $@ and next if $@;
    
    my $cnt = 1;
    foreach (@CCP4Map::header_fields) {
       my $value = $map_header{$_};
       printf "%3d. ", $cnt++;
       if(!ref($value))  {
           switch: for($_) {
               if(/cell|Density|rms/) { printf "%-15s %-7.3f\n", $_, $value }
               elsif(/mapSignature/)  { printf "%-15s '%s'\n", $_, $value }
               else                   { printf "%-15s %s\n", $_, $value }
           }
       } elsif(ref($value) eq "ARRAY" ) { 
           switch: for($_) {
               if(/symmetryOperator/) { 
                   local $" = " ],\n[ ";
                   printf "%-15s\n%30s\n", $_, "[ @$value ]";
               }
               elsif(/labels/)  { 
                   local $" = " ],\n[ ";
                   printf "%-15s\n%s\n", $_, "[ @$value ]";
               }
               else { printf "%-15s %s\n", $_, "[ @$value ]" }
           }
       }
    }
}
