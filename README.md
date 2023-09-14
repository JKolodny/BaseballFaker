# ![image](https://github.com/JKolodny/BaseballFaker/assets/24982246/a964ab4e-bf43-41b7-9c41-0b8a5e2379e9)

![image](https://github.com/JKolodny/BaseballFaker/assets/24982246/b6762139-61eb-44d4-a7c3-2762ed5c9659)

## Motivation

* Lately, when trying to work on sports analytics projects, I realize that a big
bottleneck (at least for me) is getting my hands on data. In effect, this makes it so that when I want to start a project, I try to re-learn a little about web scraping for a day or two, and then quit soon after that. 

* The value I'm trying to create here is the ability to generate simple, probably not great, but reasonable fake data for use in projects before committing to developing web scraping pipelines.

## Usage 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1i2MNvq7QqfESSEbhTfe1WYn05_WtMeK-?usp=sharing)

```
from baseballfaker.baseball import batting

batting(CAREER_LENGTH=10, 
        skill_level=.9)
```

* Example Output:
    * see __example.ipynb__:
      * ![image](https://github.com/JKolodny/SportFaker/assets/24982246/6578c484-5247-41e9-9d7f-9cd22233bb80)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)





