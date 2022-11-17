word = ''
count = 0
lst = []
sample = '''
Akali (Moderate)	Aatrox (Moderate)	Ahri (Moderate)	Akshan (Low)	Bard (High)	Alistar (Moderate)
Ekko (High)	Bel’veth (High)	Anivia (High)	Aphelios (High)	Braum (Low)	Amumu (Low)
Evelynn (High)	Camille (Moderate)	Annie (Moderate)	Ashe (Moderate)	Ivern (Moderate)	Blitzcrank (Moderate)
Fizz (Moderate)	Darius (Low)	Aurelion Sol (Moderate)	Caitlyn (Moderate)	Janna (Moderate)	Cho’gath (Moderate)	Diana (Moderate)	Azir (High)	Corki (Moderate)	Lulu (Moderate)	Galio (Moderate)
Katarina (High)	Dr. Mundo (Moderate)	Brand (Moderate)	Draven (High)	Nami (Moderate)	Jarvan IV (Moderate)
Kha’zix (Moderate)	Fiora (Low)	Cassiopeia (High)	Ezreal (Moderate)	Pyke (Moderate)	Leona (Moderate)
Leblanc (High)	Gangplank (High)	Elise (High)	Graves (Low)	Rakan (Moderate)	Malphite (Low)
Master Yi (Moderate)	Garen (Moderate)	Fiddlesticks (High)	Jhin (Moderate)	Renata Glasc (High)	Maokai (Low)
Nidalee (High)	Gnar (High)	Heimerdinger (High)	Jinx (Moderate)	Sona (Moderate)	Nautilus (Moderate)
Nocturne (Moderate)	Gragas (Moderate)	Karma (Moderate)	Kai’sa (Moderate)	Soraka (Low)	Nunu & Williump (Moderate)
Qiyana (High)	Gwen (Moderate)	Karthus (Moderate)	Kalista (Moderate)	Tahm Kench (Moderate)	Ornn (Moderate)
Rengar (High)	Hecarim (Moderate)	Kennen (Moderate)	Kindred (Moderate)	Taric (Low)	Poppy (Moderate)
Shaco (High)	Illaoi (Moderate)	Lissandra (Moderate)	Kog’maw (Moderate)	Thresh (Moderate)	Rammus (Moderate)
Talon (Moderate)	Irelia (Moderate)	Lux (Moderate)	Lucian (Moderate)	Yuumi (Low)	Rell (Low)
Viego (Moderate)	Jax (Moderate)	Malzahar (Moderate)	Miss Fortune (Low)	Zilean (Moderate)	Sejuani (Moderate)
Yone (High)	Jayce (Moderate)	Morgana (Low)	Quinn (Moderate)		Shen (Moderate)
Zed (Moderate)	Kayle (Moderate)	Neeko (Moderate)	Samira (Moderate)		Singed (Moderate)
Kayn (High)	Orianna (Moderate)	Senna (Moderate)		Sion (Moderate)
Kled (Moderate)	Ryze (Moderate)	Sivir (Moderate)		Zac (High)
Lee Sin (Moderate)	Seraphine (Low)	Teemo (Moderate)		
Lillia (High)	Swain (High)	Tristana (Moderate)		
Mordekaiser (Moderate)	Sylas (Moderate)	Twitch (Moderate)		
Nasus (Moderate)	Syndra (High)	Varus (Low)		
Nilah (High)	Taliyah (Moderate)	Vayne (High)		
Olaf (Low)	Twisted Fate (High)	Xayah (Moderate)		
Pantheon (Moderate)	Veigar (Moderate)	Zeri (Moderate)		
Rek’sai (Low)	Vel’koz (High)			
Renekton (Low)	Vex (Low)			
Riven (High)	Viktor (High)			
Rumble (High)	Vladimir (Moderate)			
Sett (Low)	Xerath (High)			
Shyvana (Moderate)	Ziggs (Moderate)			
Skarner (Moderate)	Zoe (Moderate)			
Trundle (Moderate)	Zyra (Moderate)			
Tryndamere (Moderate)				
Udyr (Moderate)				
Urgot (High)				
Vi (Moderate)				
Volibear (Low)				
Warwick (Low)				
Wukong (Low)				
Xin Zhao (Low)				
Yasuo (High)				
Yorick (Moderate)	
'''
sample = sample.replace(' (Low)', '')
sample = sample.replace(' (Moderate)', '')
sample = sample.replace(' (High)', '')
sample = sample.replace('\n', '!')
lst = sample.split('\t')
#print(len(lst))

for i in range(200):
    for n in lst:
        if n == '' or n == '!':
            lst.remove(n)

for i in lst:
    word += (i + ' ')


#word = word.partition('!')

final = word.split('!')

'''print(lst)
print(len(lst))'''
#print(word)
print(final)
#print(len(final))