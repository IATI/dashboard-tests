# ATI test 34
# Threshold applied because the introduction to proposal 4.8 uses evaluations as
# its example: they "may not be realistic or reasonable to expect for smaller
# projects". NB this indicator is NOT marked [1] in the 4.8 table, unlike the
# other thresholded tests - confirm whether that omission was deliberate.
# The figure below is provisional and needs consulting on.
@iati-activity
Feature: Documents - project performance and evaluation

  Scenario Outline: Project performance and evaluation document
    Given an IATI activity
     And the activity is current
     And `default-aid-type/@code` is not G01
     And either `document-link/category[@code="A07"]` is present, or `activity-status/@code` is one of 3 or 4
     And the activity value is at least 100000 USD
     Then `document-link/category[@code="A07"]` should be present
