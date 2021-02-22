# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import cs.ploneformdemo


class CsPloneformdemoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=cs.ploneformdemo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cs.ploneformdemo:default')


CS_PLONEFORMDEMO_FIXTURE = CsPloneformdemoLayer()


CS_PLONEFORMDEMO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CS_PLONEFORMDEMO_FIXTURE,),
    name='CsPloneformdemoLayer:IntegrationTesting',
)


CS_PLONEFORMDEMO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CS_PLONEFORMDEMO_FIXTURE,),
    name='CsPloneformdemoLayer:FunctionalTesting',
)


CS_PLONEFORMDEMO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CS_PLONEFORMDEMO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CsPloneformdemoLayer:AcceptanceTesting',
)
