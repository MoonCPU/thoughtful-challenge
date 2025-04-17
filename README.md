# thoughtful-challenge

This is my attempt at the thoughtful.ai challenge for the Forward Deployed Engineer (Latam) role.

The sort function will take in 4 params: width, height, length, mass.
- If any of width, height and length params are 150 or over, then the package is considered BULKY.
- If the weight is 20 or over that, then the package is considered HEAVY.

We can now decide the dispatch methods based on these data:
- if package is both HEAVY AND BULKY, then the dispatch method is "FORBIDDEN", as in, the package cannot be dispatched.
- if package is HEAVY or BULKY, then the dispatch method is "SPECIAL".
- if package is neither HEAVY nor BULKY, then the dispatch method is "STANDARD".
