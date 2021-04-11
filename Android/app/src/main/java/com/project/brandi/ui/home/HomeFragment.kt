package com.project.brandi.ui.home

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.View
import com.project.brandi.App
import com.project.brandi.R


class HomeFragment : Fragment(R.layout.fragment_home) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        App.prefs.getString("_id")
    }
}