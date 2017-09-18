# Lesson 3.4: Make Classes Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined in
# media.py. After you follow along with Kunal, make some instances of your own!

# After you run this code, open the file fresh_tomatoes.html to see your
# webpage!

import media  
import fresh_tomatoes

# Set up movie database
data = {
	'im': {
		'Title': 'Iron Man',
		'Release_Date': 'April 14, 2008',
		'Director': 'Jon Favreau',
		'Box_Office': '$585.2 million',
		'Plot': 'After being held captive in an Afghan cave, billionaire engineer Tony Stark '
		 + 'creates a unique weaponized suit of armour to fight evil.',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG',
		'Trailer_URL': 'https://www.youtube.com/watch?v=8hYlB38asDY'
		},

	'im2': {
		'Title': 'Iron Man 2',
		'Release_Date': 'April 26, 2010',
		'Director': 'Jon Favreau',
		'Box_Office': '$623.9 million',
		'Plot': 'With the world now aware of his identity as Iron Man, Tony Stark must contend '
		 + '''with both his declining health and vengeful mad man with ties to his father's '''
		 + 'legacy.',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/e/ed/Iron_Man_2_poster.jpg/220px-Iron_Man_2_poster.jpg',
		'Trailer_URL': 'https://www.youtube.com/watch?v=wKtcmiifycU'
		},

	'im3': {
		'Title': 'Iron Man 3',
		'Release_Date': 'May 3, 2013',
		'Director': 'Shane Black',
		'Box_Office': '$1.215 billion',
		'Plot': '''When Tony Stark's world is torn apart by a formidable terrorist called the '''
		 + 'Mandarin, he starts an odyssey of rebuilding and retribution.',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Iron_Man_3_theatrical_poster.jpg/220px-Iron_Man_3_theatrical_poster.jpg',
		'Trailer_URL': 'https://www.youtube.com/watch?v=oYSD2VQagc4'
		},

	'ca': {
		'Title': 'Captain America: The First Avenger',
		'Release_Date': 'July 22, 2011',
		'Director': 'Joe Johnston',
		'Box_Office': '$140 million',
		'Plot': 'Steve Rogers, a rejected military soldier transforms into Captain America after '
		 + '''taking a dose of a "Super-Soldier serum". But being Captain America comes at a '''
		 + 'price as he attempts to take down a war monger and a terrorist organization.',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Captain_America_The_First_Avenger_poster.jpg/220px-Captain_America_The_First_Avenger_poster.jpg',
		'Trailer_URL': 'https://www.youtube.com/watch?v=W4DlMggBPvc'
		},

	'ca2': {
		'Title': 'Captain America: The Winter Soldier',
		'Release_Date': 'March 13, 2014',
		'Director': 'Anthony Russo and Joe Russo',
		'Box_Office': '$714.3 million',
		'Plot': 'As Steve Rogers struggles to embrace his role in the modern world, he teams up '
		 + 'with a fellow Avenger and S.H.I.E.L.D agent, Black Widow, to battle a new threat from '
		 + 'history: an assassin known as the Winter Soldier.',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e8/Captain_America_The_Winter_Soldier.jpg/220px-Captain_America_The_Winter_Soldier.jpg',
		'Trailer_URL': 'https://www.youtube.com/watch?v=7SlILk2WMTI'
		},

	'ca3': {
		'Title': 'Captain America: Civil War',
		'Release_Date': 'April 12, 2016',
		'Director': 'Anthony Russo and Joe Russo',
		'Box_Office': '$1.153 million',
		'Plot': '''Political interference in the Avengers' activities causes a rift between '''
		 + 'former allies Captain America and Iron Man.',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg',
		'Trailer_URL': 'https://www.youtube.com/watch?v=dKrVegVI0Us'
		},

	'gotg': {
		'Title': 'Guardian of the Galaxy',
		'Release_Date': 'July 21, 2014',
		'Director': 'James Gunn',
		'Box_Office': '$773.3 million',
		'Plot': 'A group of intergalactic criminals are forced to work together to stop a fanatical '
		 + 'warrior from taking control of the universe.',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg',
		'Trailer_URL': 'https://www.youtube.com/watch?v=d96cjJhvlMA'
		},

	'gotg2': {
		'Title': 'Guardian of the Galaxy Vol.2',
		'Release_Date': 'May 5, 2017',
		'Director': 'James Gunn',
		'Box_Office': '$863.4 million',
		'Plot': 'The Guardians must fight to keep their newfound family together as they unravel the '
		 + '''mystery of Peter Quill's true parentage.''',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/9/95/GotG_Vol2_poster.jpg/220px-GotG_Vol2_poster.jpg',
		'Trailer_URL': 'https://www.youtube.com/watch?v=duGqrYw4usE'
		},

	'antman': {
		'Title': 'Ant-Man',
		'Release_Date': 'June 29, 2015',
		'Director': 'Peyton Reed',
		'Box_Office': '$519.3 million',
		'Plot': 'Armed with a super-suit with the astonishing ability to shrink in scale but increase in strength, '
		 + 'cat burglar Scott Lang must embrace his inner hero and help his mentor, Dr. Hank Pym, plan and pull off '
		 + 'a heist that will save the world.',
		'Poster_URL': 'https://upload.wikimedia.org/wikipedia/en/thumb/7/75/Ant-Man_poster.jpg/220px-Ant-Man_poster.jpg',
		'Trailer_URL': 'https://www.youtube.com/watch?v=pWdKf3MneyI'
		}
}

im =  media.Movie(data['im']['Title'], data['im']['Release_Date'], data['im']['Director'],
				  data['im']['Box_Office'], data['im']['Plot'], data['im']['Poster_URL'], 
				  data['im']['Trailer_URL'])

im2 =  media.Movie(data['im2']['Title'], data['im2']['Release_Date'], data['im2']['Director'],
				  data['im2']['Box_Office'], data['im2']['Plot'], data['im2']['Poster_URL'], 
				  data['im2']['Trailer_URL'])

im3 =  media.Movie(data['im3']['Title'], data['im3']['Release_Date'], data['im3']['Director'],
				  data['im3']['Box_Office'], data['im3']['Plot'], data['im3']['Poster_URL'], 
				  data['im3']['Trailer_URL'])

ca =  media.Movie(data['ca']['Title'], data['ca']['Release_Date'], data['ca']['Director'],
				  data['ca']['Box_Office'], data['ca']['Plot'], data['ca']['Poster_URL'], 
				  data['ca']['Trailer_URL'])

ca2 =  media.Movie(data['ca2']['Title'], data['ca2']['Release_Date'], data['ca2']['Director'],
				  data['ca2']['Box_Office'], data['ca2']['Plot'], data['ca2']['Poster_URL'], 
				  data['ca2']['Trailer_URL'])

ca3 =  media.Movie(data['ca3']['Title'], data['ca3']['Release_Date'], data['ca3']['Director'],
				  data['ca3']['Box_Office'], data['ca3']['Plot'], data['ca3']['Poster_URL'], 
				  data['ca3']['Trailer_URL'])

gotg =  media.Movie(data['gotg']['Title'], data['gotg']['Release_Date'], data['gotg']['Director'],
				  data['gotg']['Box_Office'], data['gotg']['Plot'], data['gotg']['Poster_URL'], 
				  data['gotg']['Trailer_URL'])

gotg2 =  media.Movie(data['gotg2']['Title'], data['gotg2']['Release_Date'], data['gotg2']['Director'],
				  data['gotg2']['Box_Office'], data['gotg2']['Plot'], data['gotg2']['Poster_URL'], 
				  data['gotg2']['Trailer_URL'])

antman =  media.Movie(data['antman']['Title'], data['antman']['Release_Date'], data['antman']['Director'],
				  data['antman']['Box_Office'], data['antman']['Plot'], data['antman']['Poster_URL'], 
				  data['antman']['Trailer_URL'])

marvelmovies = [im, im2, im3, ca, ca2, ca3, gotg, gotg2, antman]
	
fresh_tomatoes.open_movies_page(marvelmovies)

