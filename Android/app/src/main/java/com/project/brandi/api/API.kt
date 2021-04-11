package com.project.brandi.api

import com.project.brandi.data.user.CreateResponse
import com.project.brandi.data.user.LoginResponse
import com.project.brandi.data.user.UserResponse
import okhttp3.RequestBody
import retrofit2.Response
import retrofit2.http.*

// @Query = 파라미터 user?name=dd
// @Path = 경로 user/1  {_id}
// @Part = MultiPart form data

interface API {
    @GET("/api/user")
    suspend fun getUsers(
    ): Response<UserResponse>

    @Multipart
    @POST("/api/user")
    suspend fun createUser(
        @Part("user") user: RequestBody
    ): Response<CreateResponse>

    @Multipart
    @POST("/api/user/login")
    suspend fun loginUser(
        @Part("user") user: RequestBody
    ): Response<LoginResponse>
}