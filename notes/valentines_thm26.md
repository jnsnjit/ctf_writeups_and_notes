# TryHackMe 2026 - Valentines CTF #

## Challenge 1 - Valenfind ##
__Category: WEB__ <br>
__Description:__ There’s this new dating app called “Valenfind” that just popped up out of nowhere. I hear the creator only learned to code this year; surely this must be vibe-coded. Can you exploit it? <br>

vibe-coded and title seem like starting hints, will keep them in mind. <br>

most likely constructed with nodejs or flask based of the port 5000. <br>

session=eyJsaWtlZCI6W10sInVzZXJfaWQiOjksInVzZXJuYW1lIjoiYWRtaW4ifQ.aY-1Tw.0ZC7qePGSNvdp_6x9fwsT--ilpo <br>

when liking profiles, directory is /like/#

cupid=8
/api/fetch_layout
/like
/dashboard
/my_profile
/logout

there is some type database being utilized