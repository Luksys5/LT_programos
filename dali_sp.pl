#!/usr/bin/perl -w
#BEGIN {push @INC, '/home/lukas/pdb/visi'}
#use EPMS;
use lib '/home/lukas/pdb/visi';
use FindBin;
use Getopt::Long;
use lib "$FindBin::Bin";
use File::Basename;
use Getopt::Long;
use Misc::Parse;
use strict;

import File::Basename qw/basename dirname/;

my   $help = <<EOINPUT;

Performs DaliLite superposition of a target pdb file to enumerated 
template ones; DaliLite output is converted to FASTA format.

Usage:
$0 <Parameters>

Parameters:
-i <pdb_file>
              filename of a target pdb file
-l <pdb_templates>
              file that contains a list of template pdb files to be
              superimposed to the target pdb file
-o <output_dir>
              directory where the output files will be placed in
    default=  directory where <pdb_file> locates in
-m <output_file>
              full name of a file where all sequences in fasta format 
              will be flushed in
    default=  STDOUT
-h
              this text

EOINPUT

#-t
#              clear all redundant intermediate files; there will only 
#              be left original pdb-, newly generated pdb and fasta
#              files


@ARGV || die("$help\n");


my  $target_pdb;
my  $templates_pdb;
my  $output_dir;
my  $output_file;
my  $clear;

GetOptions( "i=s" => \$target_pdb, "l=s" => \$templates_pdb, "o:s" => \$output_dir,
	    "m:s" => \$output_file,
	    't' => sub { $clear = 1; },
            'h' => sub { print("$help\n"); exit; });

( $target_pdb && $templates_pdb ) || die("$help\n");

if( $output_dir && ! -e $output_dir ) {
    system( "mkdir $output_dir" ) && die( "cannot create directory $output_dir: $!\nexit\n" );
}

$output_dir = `dirname $target_pdb` if !$output_dir; chomp $output_dir; 
die "error while attempting to determine output directory\nexit\n" unless -e $output_dir && -d _;


print "target file = $target_pdb\n",
      "templates pdb file = $templates_pdb\n",
      "output_dir = $output_dir\n\n";


my $dali='/home/lukas/daliserver/DaliLite_3.3/DaliLite';

my $inline;
my @structures;

# ------------------------------------------------------------------------------
# Read pdb file list from the file
#

open( LIST, $templates_pdb ) || ( print( "Cannot open input list file $templates_pdb\n" ) && die );

while( $inline = <LIST> ) {
    chomp( $inline );
    next if $inline =~ /^#/ || length $inline < 2;
    $inline =~ s/^\s+//;
    $inline =~ s/\s+$//;
    push @structures, $inline;
}
close( LIST );

coverByDali( @structures ); 

# ------------------------------------------------------------------------------

sub coverByDali {
    my  @structures = @_;

    my  $cmd; 
    my  $log_file = "${output_dir}/log";
    my ($new_name, $new_name1, $new_name2);

    my %sequences;
    my @orderarray;

    my $which = 0; 
    my $suffix = '_dssp';

    $new_name1 = basename( $target_pdb ); 
    $new_name1 =~ s/\.\w+$//; # trim extension

    foreach my $struct (@structures) {

	$cmd = "$dali -pairwise $target_pdb $struct";
	print "Superimposing $target_pdb and $struct...\n\n";
	if( system("$cmd > $log_file")) {
	    print "system $cmd failed: $?\n"; 
	    next;
	}
	$new_name2 = basename( $struct ); $new_name2 =~ s/\.\w+$//; # trim extension
	my $Mol_name = "${new_name1}_${new_name2}_dali.pdb";
	system( "mv mol2_1.pdb $output_dir/$Mol_name" ) && 
	    (print "error while producing $Mol_name\n"&& next);

	my $Aln_name = $new_name1.'_'.$new_name2.'_dali_ali.html';
	system( "mv aln.html $output_dir/$Aln_name" ) && 
	    (print "error while producing $Aln_name\n"&& next);
	
	print "\t(converting html -> fasta ...)\n";
	convertOutput( "$output_dir/$Aln_name", $new_name1, $new_name2, $suffix, 
		       \%sequences, \@orderarray, $which++ ); 

	my $CA_name = $new_name1.'_'.$new_name2.'_CA.pdb';
	system( "mv CA_1.pdb $output_dir/$CA_name" ) && 
	    (print "error while producing $CA_name\n"&& next);

	my $Ind_name = $new_name1.'_'.$new_name2.'_index.html';
	system( "mv index.html $output_dir/$Ind_name" ) && 
	    (print "error while producing $Ind_name\n"&& next);

	correctIndexContents( "$output_dir/$Ind_name", $Mol_name, $Aln_name, $CA_name ); 
	
    }	

    `rm $output_file` if $output_file && -e $output_file && -f _;

    foreach( @orderarray ) {
	next unless exists $sequences{$_};
	Parse::writeFasta( $output_file, { $_ => $sequences{$_}} );
	delete $sequences{$_} if $_ =~ /$new_name1/;
    }
}

# ------------------------------------------------------------------------------

sub correctIndexContents {
    my $ind_name = shift;
    my $mol_name = shift;
    my $aln_name = shift;
    my $ca_name  = shift;

    my $line;
    my $text;

    open( HTM, "<$ind_name" ) || die( "cannot open file: $!\n");

    while($line = <HTM>) {
	$text .= $line;
    }
    close( HTM );

    $text =~ s/aln\.html/$aln_name/g;
    $text =~ s/CA_1\.pdb/$ca_name/g;
    $text =~ s/mol2_1\.pdb/$mol_name/g;

    open( HTM, ">$ind_name" ) || die( "cannot open file: $!\n");
    print HTM $text; 
    close( HTM );
}


# ------------------------------------------------------------------------------

sub convertOutput {
    my  $filename = shift;
    my  $target   = shift;
    my  $subject  = shift;
    my  $suffix   = shift;
    my	$refS  	  = shift;   # reference to the hash
    my	$refA	  = shift;   # reference to the array
    my  $which    = shift;   # running number of file being processed

    my  @temp_array; 
    my  %temp_seque;
    my ( $key, $value );
    my  $new_name = $filename; 

    readDaliHtml( $filename, $target, $subject, $suffix, \%temp_seque, \@temp_array ); 
    Parse::translateSequences( \%temp_seque ); 
    dsspLoopSymbols( \%temp_seque, $suffix ); 

    $new_name =~ s/\.\w*$//;
    $new_name.= '.fa'; 

    `rm $new_name` if -e $new_name && -f _;
    foreach( @temp_array ) {
	Parse::writeFasta( $new_name, { $_ => $temp_seque{$_}} );
    }
    
    condenseToMultipleAlignment( \%temp_seque, $target, $suffix );

##    $$refS{"$target$which"} = $temp_seque{$target};
##    $$refS{"$target$suffix$which"} = $temp_seque{"$target$suffix"};

    while(( $key,$value ) = each %temp_seque ){ $$refS{$key} = $value; }
    push @{ $refA }, @temp_array ;
}

# ------------------------------------------------------------------------------

sub readDaliHtml {
    my	$filename = shift; 
    my  $querytit = shift;
    my  $sbjcttit = shift;
    my  $suffix   = shift;   # dssp suffix for title
    my	$refS  	  = shift;   # reference to the hash
    my	$refA	  = shift;   # reference to the array
    my  $index = 0;          # reference to running index of the array
    my  %lochash;
    my	$line; 
    my	$exp = qr/^<PRE>/;
    my 	$end = qr/^<\/PRE>/;
    my	$ind = 0; 
    my	$cond = 0;


    open( HTM, "< " . $filename ) || die( "cannot open file: $!\n");

WHILE:
    while($line = <HTM>) {
	if( $line =~ $exp ) { $cond = 1;  next; };
        next if !$cond;
	last if $line =~ $end;
	
	next unless $line =~ /^([^\s\t]+)[\s\t]+([^\s\t]+)([\s\t]+\d+)?$/;
	my $title = $1;
	my $seque = $2;
        SWITCH: {
            ( $title =~ /^DSSP$/i ) && do { 
		unless( $ind++ % 2 ) { $title = "$querytit$suffix"; }   # even occurence 
		else { $title = "$sbjcttit$suffix"; }   # odd occurence
		last SWITCH;
	    };
            ( $title =~ /^Query$/i ) && do { $title = "$querytit"; last SWITCH; };
            ( $title =~ /^Sbjct$/i ) && do { $title = "$sbjcttit"; last SWITCH; };
	    next WHILE; 
        }

	unless( $lochash{$title}) {
	    $$refA[$index++]= $title;
	    $lochash{$title}=1;
	}
	$$refS{$title} .= $seque;
    }
    close( HTM );
}

# ------------------------------------------------------------------------------
# sequences passed are supposed to be already translated to FASTA format
#
sub condenseToMultipleAlignment {
    my	$hr_seqs = shift;   # reference to hash of sequences 
    my  $s_title = shift;   # of target sequence 
    my  $suffix  = shift;   # suffix added to the dssp sequence
    my	$columns = length $$hr_seqs{$s_title}; 
    my	$gap; 
    my	$res; 
    my	$it = 0; 

    while( $it < $columns ) {
	$res = substr( $$hr_seqs{$s_title}, $it, 1 ); 
	$res = '\.' if $res eq '.'; 
	$gap = !scalar grep {/$res/i} keys %Parse::aaSingle;

        foreach my $title ( keys %{ $hr_seqs }) {
	    $res = substr( $$hr_seqs{$title}, $it, 1 ); 
	    $res = '\.' if $res eq '.'; 
	    if( $gap ) {
		substr( $$hr_seqs{$title}, $it, 1 )= ''; 
		next;
	    }
	    substr( $$hr_seqs{$title}, $it, 1 )= '-' if $title =~ /$suffix$/ && $res =~ /l/i;
	    # the latter statement overwrites 'L' symbol of the dssp sequence with '-'
	}
	unless( $gap ) { $it++; }
	else { $columns--; }
    }
}

# ------------------------------------------------------------------------------

sub dsspLoopSymbols {
    my  $hr_seqs = shift;
    my  $suffix  = shift;
    foreach my $title ( keys %{$hr_seqs} ) {
	next unless $title =~ /$suffix$/; 
	for my $it ( 0 .. length( $$hr_seqs{$title}) - 1 ) {
	    substr( $$hr_seqs{$title}, $it, 1 )= '-' if substr( $$hr_seqs{$title}, $it, 1 ) =~ /l/i;
	}
    }
}
