# No ATI equivalent
# TODO validate the codes against their codelists. Country and Region are separate
# codelists, and both codelist steps raise when the element is absent, so asserting
# each in turn would wrongly fail an activity that uses only the other. This needs
# either a guard step ("only if X is present") or a combined codelist step.
@iati-activity
Feature: Country or region

  Scenario Outline: Country or region is present
    Given an IATI activity
     And the activity is current
     Then `recipient-country | recipient-region | transaction/recipient-country | transaction/recipient-region` should be present
