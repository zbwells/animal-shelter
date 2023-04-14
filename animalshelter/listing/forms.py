## Zander B. Wells <zbwells@protonmail.com>
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.

from django import forms

## Making forms using Django's form generator, to be consistent with the admin page.
## At least to some extent.

## May need to edit this page depending on client input...
## Since the options are hard-coded for now.

class FilterForm(forms.Form):
    order = forms.ChoiceField( 
        label = "Sort by",
        choices = (
            ("intake_date", "Intake Date"),
            ("name", "Name"), 
            ("estimated_age", "Age"),
            ("gender", "Gender"),
            ("species", "Species"),
            ("breed", "Breed"),
            ("weight", "Weight"),
        )
    )

    # Part of the form to ask the user what ages of animals they would like to see
    filter_by_age = forms.ChoiceField(
        label = "Filter by Age",
        choices = (
            ("any-age", "Any"),
            ("zero-to-two-months", "0 - 2 Months"),
            ("three-to-six-months", "3 - 6 Months"),
            ("seven-to-eleven-months", "7 - 11 Months"),
            ("one-to-two-years", "1 - 2 Years"),
            ("two-or-more-years", "2 or more Years"),
            ("three-or-more-years", "3 or more Years"),
        )
    )

    # Same as previous, but for species; currently only dogs and cats
    filter_by_species = forms.ChoiceField(
        label = "Filter by Species",
        choices = (
            ("any-species", "Any"),
            ("dog", "Dogs"),
            ("cat", "Cats"),
        )
    )
           
    
