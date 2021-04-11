package com.project.brandi.data.user

import com.project.brandi.api.RetrofitInstance
import okhttp3.RequestBody

class UserRepository {
    suspend fun createUser(user: RequestBody) =
        RetrofitInstance.api.createUser(user)

    suspend fun loginUser(user: RequestBody) =
        RetrofitInstance.api.loginUser(user)
}