#Comparing each Simpsons season by IMDB ratings

from pylab import plot, show
import math

#simpsons year 1989 only has 1 episode
simpsons_1989 = [8.2]
simpsons_1990 = [7.9]
simpsons_1991 = [8.1]
simpsons_1992 = [8.3]
simpsons_1993 = [8.4]
simpsons_1994 = [8.2]
simpsons_1995 = [8.5]
simpsons_1996 = [8.3]
simpsons_1997 = [8.1]
simpsons_1998 = [7.4]
simpsons_1999 = [7.5]
simpsons_2000 = [7.3]
simpsons_2001 = [7.4]
simpsons_2002 = [7.1]
simpsons_2003 = [7.1]
simpsons_2004 = [7.1]
simpsons_2005 = [7.0]
simpsons_2006 = [6.9]
simpsons_2007 = [7.0]
simpsons_2008 = [6.9]
simpsons_2009 = [6.9]
simpsons_2010 = [6.8]
simpsons_2011 = [6.9]
simpsons_2012 = [6.7]
simpsons_2013 = [6.7]
simpsons_2014 = [6.9]
simpsons_2015 = [6.8]
simpsons_2016 = [6.7]
simpsons_2017 = [6.7]
simpsons_2018 = [6.7]
#was only on 13 episodes at this time.
simpsons_2019 = [6.1]


simpsons_total_avg = [8.2, 7.9, 8.1, 8.3, 8.4, 8.2, 8.5, 8.3, 8.1, 7.4, 7.5, 7.3, 7.4, 7.1, 7.1, 7.1, 7.0, 6.9, 7.0, 6.9, 6.9, 6.8, 6.9, 6.7, 6.7, 6.9, 6.8, 6.7, 6.7, 6.7, 6.1]
years = range(1989, 2020)
plot(years, simpsons_total_avg, marker='o')
show()
