# Released under the MIT License. See LICENSE for details.
#
"""Contains AppModeSelector base class."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from babase._appintent import AppIntent
    from babase._appmode import AppMode


class AppModeSelector:
    """Defines which AppModes are available or used to handle given AppIntents.

    Category: **App Classes**

    The app calls an instance of this class when passed an AppIntent to
    determine which AppMode to use to handle the intent. Plugins or
    spinoff projects can modify high level app behavior by replacing or
    modifying the app's mode-selector.
    """

    def app_mode_for_intent(self, intent: AppIntent) -> type[AppMode] | None:
        """Given an AppIntent, return the AppMode that should handle it.

        If None is returned, the AppIntent will be ignored.

        This may be called in a background thread, so avoid any calls
        limited to logic thread use/etc.
        """
        raise NotImplementedError()

    def testable_app_modes(self) -> list[type[AppMode]]:
        """Return a list of modes to appear in the dev-console app-mode ui.

        The user can switch between these app modes for testing. App-modes
        will be passed an AppIntentDefault when selected by the user.

        Note that in normal circumstances AppModes should never be
        selected explicitly by the user but rather determined implicitly
        based on AppIntents.
        """
        raise NotImplementedError()
