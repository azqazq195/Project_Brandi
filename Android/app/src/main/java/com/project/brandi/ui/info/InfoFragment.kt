package com.project.brandi.ui.info

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.navigation.findNavController
import com.project.brandi.R

class InfoFragment : Fragment(R.layout.fragment_info) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        view.findViewById<TextView>(R.id.tvSignIn).setOnClickListener{
            view.findNavController().navigate(
                R.id.action_infoFragment_to_signInFragment
            )
        }

        view.findViewById<TextView>(R.id.tvSignUP).setOnClickListener {
            view.findNavController().navigate(
                R.id.action_infoFragment_to_signUpFragment
            )
        }
    }
}