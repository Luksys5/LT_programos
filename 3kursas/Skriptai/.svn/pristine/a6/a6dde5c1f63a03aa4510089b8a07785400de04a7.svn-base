#!/usr/bin/perl -w
################################################################################
#                                                                              #
#                             cute_surface.pl                                  #
#                             ===============                                  #
#                                                                              #
# convert from ungrasp'ed surface to smoothly interpolated surface file.       #
#                                                                              #
#                 use: cute_surface.pl <filename> > outfile.r3d                #
#                                                                              #
#                                                           v1.0 jtk 20.10.99  #
#                                                                              #
################################################################################

use strict;

my $cnt = 0;
my @tmp;
my @vertices;
my @points;
my @sorted_points;
my %unique_points;
my $cn2;

################################################################################
#                                                                              #
#                                SORT-ROUTINE                                  #
#                                                                              #
################################################################################
sub by_position
{ 
  my $result ;

  $result = $a->[0] <=> $b->[0];
  return $result if $result != 0;
  $result = $a->[1] <=> $b->[1];
  return $result if $result != 0;
  $result = $a->[2] <=> $b->[2];
  return $result if $result !=0;
}


################################################################################
#                                                                              #
#                     READ in array of arrays named @tmp                       #
#                                                                              #
################################################################################

while ( <> )
{ 
  my @tmp1 ;

  @tmp1 = split(' ',$_,13) ;
  push( @tmp, [ @tmp1 ] );
 
  print STDERR "r" if $. % 1000 == 0;
}

print STDERR "\n";

################################################################################
#                                                                              #
#                           CREATE DATASTRUCTURES                              #
#                                                                              #
# @vertices                                                                    #
#     as array (by triangle) of arrays (by prop x1,y1,z1..z3,r,g,b,vnx1..vnxz3)#
# @points                                                                      #
#     as array (by index)    of arrays (by prop x,y,z,r,g,b)                   #
#                                                                              #
################################################################################
$cnt = 0;
$cn2 = 0;
while ( $cnt <= $#{tmp} )  
{  
  
  push ( @vertices,[ @{$tmp[$cnt+1]}, @{$tmp[$cnt+3]}] );
  push ( @points, [@{$vertices[$cn2]}[0..2,9..11]] );
  push ( @points, [@{$vertices[$cn2]}[3..5,9..11]] );
  push ( @points, [@{$vertices[$cn2]}[6..8,9..11]] );
  
  $cnt += 4;
  $cn2 += 1;
  print STDERR "." if $cn2 % 1000 == 0;
}

print STDERR "\n";

################################################################################
#                                                                              #
#                 SORT @points into @sorted_points ...                         #
#..............................................................................#
@sorted_points = sort by_position @points;
#..............................................................................#
#                                                                              #
#                       and UNIQUEIFY into                                     #
#                                                                              #
# %unique_points as hash of hashes of form:                                    #
# %unique_points = {                                                           #
#                    "$x$y$z" => {                                             #
#                                  "r"    => rval,                             #
#                                  "g"    => gval,                             #
#                                  "b"    => bval,                             #
#                                  "nump" => numpoints                         #
#                                {                                             #
#                  }                                                           #
#                                                                              #
################################################################################
$cnt = 1;
  my $tidx="${$sorted_points[0]}[0] ${$sorted_points[0]}[1] ${$sorted_points[0]}[2]";
    ${$unique_points{$tidx}}{r}     = ${$sorted_points[0]}[3];
    ${$unique_points{$tidx}}{g}     = ${$sorted_points[0]}[4];
    ${$unique_points{$tidx}}{b}     = ${$sorted_points[0]}[5];
    ${$unique_points{$tidx}}{nump}  = 1;
while ( $cnt <= $#sorted_points )
{
  my $cno=$cnt - 1;
  my $nidx="${$sorted_points[$cnt]}[0] ${$sorted_points[$cnt]}[1] ${$sorted_points[$cnt]}[2]";
  my $oidx="${$sorted_points[$cno]}[0] ${$sorted_points[$cno]}[1] ${$sorted_points[$cno]}[2]";

  if ( "$nidx" eq "$oidx" )
  { 
      ${$unique_points{$nidx}}{r}     = ${$unique_points{$nidx}}{r}+${$sorted_points[$cnt]}[3];
      ${$unique_points{$nidx}}{g}     = ${$unique_points{$nidx}}{g}+${$sorted_points[$cnt]}[4];
      ${$unique_points{$nidx}}{b}     = ${$unique_points{$nidx}}{b}+${$sorted_points[$cnt]}[5];
      ${$unique_points{$nidx}}{nump}  = ${$unique_points{$nidx}}{nump}+1;
  }
  else
  {
    ${$unique_points{$nidx}}{r}     = ${$sorted_points[$cnt]}[3];
    ${$unique_points{$nidx}}{g}     = ${$sorted_points[$cnt]}[4];
    ${$unique_points{$nidx}}{b}     = ${$sorted_points[$cnt]}[5];
    ${$unique_points{$nidx}}{nump}  = 1;
  }
  $cnt++;
  print STDERR "." if $cnt % 1000 == 0;
}        

print STDERR "\n";

#################################################################################
#                                                                               #
#                   PRINT in raster3d format to STDOUT                          #
#                                                                               #
#################################################################################
$cnt = 0;
while ( $cnt <= $#vertices )
{
  my $x1  = ${$vertices[$cnt]}[0];  
  my $y1  = ${$vertices[$cnt]}[1];  
  my $z1  = ${$vertices[$cnt]}[2];
#..........................................
  my $x2  = ${$vertices[$cnt]}[3];  
  my $y2  = ${$vertices[$cnt]}[4];  
  my $z2  = ${$vertices[$cnt]}[5];
#..........................................
  my $x3  = ${$vertices[$cnt]}[6];  
  my $y3  = ${$vertices[$cnt]}[7];  
  my $z3  = ${$vertices[$cnt]}[8];
#==========================================  
  my $xn1 = ${$vertices[$cnt]}[13];  
  my $yn1 = ${$vertices[$cnt]}[14];  
  my $zn1 = ${$vertices[$cnt]}[15];
#..........................................
  my $xn2 = ${$vertices[$cnt]}[16];  
  my $yn2 = ${$vertices[$cnt]}[17];  
  my $zn2 = ${$vertices[$cnt]}[18];
#..........................................
  my $xn3 = ${$vertices[$cnt]}[19];  
  my $yn3 = ${$vertices[$cnt]}[20];  
  my $zn3 = ${$vertices[$cnt]}[21];
#==========================================  
  my $idx1= "$x1 $y1 $z1";
   my $r1  =  ${$unique_points{$idx1}}{r}/${$unique_points{$idx1}}{nump};
   my $g1  =  ${$unique_points{$idx1}}{g}/${$unique_points{$idx1}}{nump};
   my $b1  =  ${$unique_points{$idx1}}{b}/${$unique_points{$idx1}}{nump};
#..........................................
  my $idx2= "$x2 $y2 $z2";
   my $r2  =  ${$unique_points{$idx2}}{r}/${$unique_points{$idx2}}{nump};  
   my $g2  =  ${$unique_points{$idx2}}{g}/${$unique_points{$idx2}}{nump}; 
   my $b2  =  ${$unique_points{$idx2}}{b}/${$unique_points{$idx2}}{nump};
#..........................................
  my $idx3= "$x3 $y3 $z3";
   my $r3  =  ${$unique_points{$idx3}}{r}/${$unique_points{$idx3}}{nump};
   my $g3  =  ${$unique_points{$idx3}}{g}/${$unique_points{$idx3}}{nump};  
   my $b3  =  ${$unique_points{$idx3}}{b}/${$unique_points{$idx3}}{nump};

  printf "1\n%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f 0.00 0.00 0.00\n",$x1,$y1,$z1,$x2,$y2,$z2,$x3,$y3,$z3;
  printf "7\n%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f\n",$xn1,$yn1,$zn1,$xn2,$yn2,$zn2,$xn3,$yn3,$zn3;
  printf "17\n %5.2f %5.2f %5.2f %5.2f %5.2f %5.2f %5.2f%5.2f%5.2f\n",$r1,$g1,$b1,$r2,$g2,$b2,$r3,$g3,$b3;
# alternative:   printf "17\n" . (" %5.2f" x 9) ."\n",$r1,$g1,$b1,$r2,$g2,$b2,$r3,$g3,$b3;
  $cnt ++;
 
}


