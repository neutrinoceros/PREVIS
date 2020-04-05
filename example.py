#!/usr/bin/env python
import previs

# Perform previs research on one object:
data = previs.search('Altair')

# Plot the observability from VLTI and CHARA
fig = previs.plot_VLTI(data)
fig.show()

fig = previs.plot_CHARA(data)
fig.show()

# Perform previs research on a list of stars:
stars = ['Betelgeuse', 'Altair']

survey = previs.survey(stars, namelist='survey_example', upload=True)

# Count the observable star with each instruments (mode, telescope, spectral resolution, etc.)
result_survey, list_no_simbad = previs.count_survey(survey)

# If some stars of the list are not in the Simbad database, they will appear here:
if len(list_no_simbad) > 0:
    print('Warning: some stars are not in Simbad:', 'red')
    print(list_no_simbad)

# Print the list of observable stars (sum up):
print(result_survey)

# plot the histogram of the survey:
fig = previs.plot_histo_survey(result_survey)

fig.show()
