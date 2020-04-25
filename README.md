## Random Champ Selector

```json
{
  "Version": "2.0.0",
  "Python_Version": "3.8.0",
  "Requirements": {
    "requests": "2.22.0"
  }
}
```

Ever been in a situation where you are running a 1v1 League of Legends tournament and you want everyone to be randomly paired assigned a random set of champions?

Maybe there are even a group of champions that you all hate so much that you don't want to see them in your tournament.


With this tool, you can achieve all this.

Before you run, you need to install requests:
```bash
pip install -U requests
```

Clone this repo, and run the `lol_1v1_tournament_generator.py` file.

It will ask how many players there are, and how many champions you want each player to have and it will create your matches.

It will call the Riot API and check that the champ file it still up to date. If not, it will updated it with the newly released champs.
It will also then ask to update your ban template file as well.

To stop any champs from being randomly picked, simply go in to the `banned_champs.txt` file and remove the `#` from in front of their name.

Once a round it complete, it will ask you to enter the winners of the matches and then generate a new set of matches and a new set of champs.