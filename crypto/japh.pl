#!/usr/bin/perl
$| = 1;print "Welcome to the house of the shÃ¨n!\n";
print "Find the wisdom through the Perl.  Control is key.\n";
https://www.youtube.com/watch?v=fxR-rTe_ahEmy 

#$s is user input, stdin function, similiar to c
$s = <STDIN>;chomp($s);
#this regex command takes the user input, and does "smashing, which takes duplicate
#chars next to each and remove duplicates"
$s =~ y/0-9A-Za-z/0-9A-Za-z/s;

#char length must be greater then 216
if (length($s) < 216) {print("Cease your meddling! This will be your tomb!\n");
    exit;
}
#takes string and performs this
my $b = substr($s, $s-1, $s);
#takes substr input, finds number (we want at 128 chars, so minus one --> type 129)
$b = substr($b, $b+1, $b);
#then takes from that 128, we want 64, but plus one, so type 63)

#four regex functions, only really removes and replaces values that arent relevant
$b =~ s/R/0/g;$b =~ s/([H-S])/\c8/g;
$b =~ s/([i-t])/uc($1)/ge;
$b =~ s/x/R/ge;
my $d = $b;
#performs text ROT of 13 chars
$d =~ y/4-p/A-{/;

#opens answer file, compares, if correct, print flag
my $file = 'japh.txt';
open(FH, '<', $file) or die $!;
$f = <FH>;
if($f eq $d) {
    $file = 'flag.txt';
    open(FH, '<', $file) or die $!;
    while(<FH>) {print $_;}
}