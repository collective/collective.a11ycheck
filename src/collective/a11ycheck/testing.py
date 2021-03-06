# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import collective.a11ycheck


class CollectiveA11YcheckLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.a11ycheck)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.a11ycheck:default')


COLLECTIVE_A11YCHECK_FIXTURE = CollectiveA11YcheckLayer()


COLLECTIVE_A11YCHECK_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_A11YCHECK_FIXTURE,),
    name='CollectiveA11YcheckLayer:IntegrationTesting',
)


COLLECTIVE_A11YCHECK_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_A11YCHECK_FIXTURE,),
    name='CollectiveA11YcheckLayer:FunctionalTesting',
)


COLLECTIVE_A11YCHECK_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_A11YCHECK_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveA11YcheckLayer:AcceptanceTesting',
)
