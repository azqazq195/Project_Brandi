package com.project.brandi

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.drawerlayout.widget.DrawerLayout
import androidx.navigation.fragment.NavHostFragment
import androidx.navigation.fragment.findNavController
import androidx.navigation.ui.setupWithNavController
import com.google.android.material.bottomnavigation.BottomNavigationView

class MainActivity : AppCompatActivity() {

    private lateinit var bottomNavigationView: BottomNavigationView
    private lateinit var mainNavHostFragment: NavHostFragment

    lateinit var drawerLayout: DrawerLayout
    lateinit var mainLayoutRoot: ConstraintLayout

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mainLayoutRoot = findViewById(R.id.mainLayoutRoot)
        bottomNavigationView = findViewById(R.id.bottomNavigationView)

        mainNavHostFragment = supportFragmentManager.findFragmentById(R.id.mainNavHostFragment) as NavHostFragment
        bottomNavigationView.setupWithNavController(mainNavHostFragment.findNavController())
    }
}