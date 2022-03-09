# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.a11ycheck.testing import (
    COLLECTIVE_A11YCHECK_INTEGRATION_TESTING  # noqa: E501,
)
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.a11ycheck is properly installed."""

    layer = COLLECTIVE_A11YCHECK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.a11ycheck is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.a11ycheck'))

    def test_browserlayer(self):
        """Test that ICollectiveA11YcheckLayer is registered."""
        from collective.a11ycheck.interfaces import (
            ICollectiveA11YcheckLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveA11YcheckLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_A11YCHECK_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.a11ycheck'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.a11ycheck is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.a11ycheck'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveA11YcheckLayer is removed."""
        from collective.a11ycheck.interfaces import \
            ICollectiveA11YcheckLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveA11YcheckLayer,
            utils.registered_layers())
